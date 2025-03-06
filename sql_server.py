# import MySQLdb
from sql_server_gui import *
import pandas as pd
from datetime import datetime


class ServerData:
    def __init__(self, host='', user='', password='', database=''):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = ""
        self.cursor = ""
        self.table_name_acc_data = 'accelerometers_data'
        self.table_name_map_data = 'maps_data'
        self.table_photos_data = 'photos_data'
        self.table_results_data = 'results_data'
        self.results_data = pd.DataFrame()
        self.project_list = []
        self.accelerometer_list = []
        self.df_acc = pd.DataFrame(columns=['Acelerometro', 'Time', 'Eje_X', 'Eje_Y', 'Eje_Z'])

    def clean_variables(self):
        self.table_name_acc_data = 'accelerometers_data'
        self.table_name_map_data = 'maps_data'
        self.table_photos_data = 'photos_data'
        self.table_results_data = 'results_data'
        self.database = ''
        self.project_list = []
        self.accelerometer_list = []
        self.df_acc = pd.DataFrame(columns=['Acelerometro', 'Time', 'Eje_X', 'Eje_Y', 'Eje_Z'])

    def connect(self):
        try:
            print('Connecting to:', self.host)
        #     if self.database != '':
        #         try:
        #             self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password,
        #                                         db=self.database)
        #         except MySQLdb.Error:
        #             self.conn = MySQLdb.connect(unix_socket='/var/run/mysqld/mysqld.sock', host=self.host,
        #                                         user=self.user, passwd=self.password,
        #                                         db=self.database)
        #         print('Connected as:', self.user)
        #     else:
        #         try:
        #             self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password)
        #         except MySQLdb.Error:
        #             self.conn = MySQLdb.connect(unix_socket='/var/run/mysqld/mysqld.sock', host=self.host,
        #                                         user=self.user, passwd=self.password)
        #         print('Connected as:', self.user)
        #         print('Waiting for database')
        #     self.cursor = self.conn.cursor()
        except:
            print('Connecting error')

    def disconnect(self):
        try:
            if self.cursor != '':
                self.cursor.close()
            if self.conn != '':
                self.conn.close()
            print('Disconnected')
        except:
            print('Disconnecting error')

    def list_tables(self):
        self.disconnect()
        self.connect()
        query = "SHOW DATABASES"
        self.cursor.execute(query)
        tuple_projects = self.cursor.fetchall()
        self.project_list = []
        for i in range(len(tuple_projects)):
            if tuple_projects[i][0] != 'mysql' and tuple_projects[i][0] != 'information_schema' and tuple_projects[i][
                0] != 'performance_schema' and tuple_projects[i][0] != 'sys':
                self.project_list.append(tuple_projects[i][0])
        self.project_list = self.project_list[:len(self.project_list)]

    def set_project(self, database):
        self.database = database

    def list_accelerometers(self):
        self.disconnect()
        self.connect()
        query = "SELECT DISTINCT ID FROM " + self.table_name_acc_data
        print(query)
        self.cursor.execute(query)
        tuple_accelerometers = self.cursor.fetchall()
        for i in range(len(tuple_accelerometers)):
            self.accelerometer_list.append(tuple_accelerometers[i][0])
        print(self.accelerometer_list)

    def consult_accelerometer(self, acc_list, limit=0):
        self.disconnect()
        self.connect()
        query = "SELECT * FROM " + self.table_name_acc_data + " WHERE ID IN ('"
        for ace in acc_list:
            query += ace + "', '"
        query = query[:len(query) - 3] + ");"
        if limit > 0:
            query = query[:len(query) - 1] + " ORDER BY tiempo DESC LIMIT " + str(limit) + ";"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.df_acc = pd.DataFrame(results, columns=['Acelerometro', 'Time', 'Eje_X', 'Eje_Y', 'Eje_Z'])

    def take_project_coordinates(self):
        self.disconnect()
        self.connect()
        query = "SELECT * FROM " + self.table_name_map_data + ';'
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        latitude = results[0][0]
        longitude = results[0][1]
        return latitude, longitude

    def take_project_photo_pathdir(self):
        self.disconnect()
        self.connect()
        query = "SELECT * FROM " + self.table_photos_data + ';'
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        pathdir = results[0][0]
        return pathdir

    def insert_results(self, method, included, modes):
        self.disconnect()
        self.connect()
        date_time = datetime.now()
        modes_str = ''
        for value in modes:
            modes_str = modes_str + "{:.3f}".format(value) + ', '
        modes_str = modes_str[:len(modes_str) - 2]
        query = "INSERT INTO " + self.table_results_data + " (date, method, included, modes) VALUES ('" + str(
            date_time) + "', '" + method + "', '" + included + "', '" + modes_str + "');"
        self.cursor.execute(query)
        self.conn.commit()

    def take_results(self):
        self.disconnect()
        self.connect()
        query = "SELECT * FROM " + self.table_results_data + ";"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.results_data = pd.DataFrame(results, columns=['Date', 'Method', 'Included', 'Modes'])


class MyDataBaseDialog(QtWidgets.QDialog):
    def __init__(self, user='main', parent=None, host='localhost', password='cimne2020'):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEditUser.setText(user)
        self.ui.lineEditHost.setText(host)
        self.ui.lineEditPassword.setText(password)
        self.ui.pushButtonConnect.clicked.connect(self.connection)
        self.ServerData = ServerData()

    def connection(self):
        self.ServerData.host = self.ui.lineEditHost.text()
        self.ServerData.user = self.ui.lineEditUser.text()
        self.ServerData.password = self.ui.lineEditPassword.text()
        self.ServerData.database = ''
        super().accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
