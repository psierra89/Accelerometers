from iniciarAcel_UDP_gui_OPENARMS import *
import sys
import time
import socket
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
import threading
# import MySQLdb
import sql_server
# import liveplot as lvplt
# import matplotlib.pyplot as plt

def obtain_time():
    comparator = time.time()
    comparator_int = int(comparator)
    gap = 3
    flag = True
    while flag:
        value = time.time()
        if value - comparator_int >= gap:
            flag = False
    return int(value)


def insert_value(cursor, conn, id, time, axis_X, axis_Y, axis_Z, table_name):
    try:
        query = "INSERT INTO " + table_name + " (ID, tiempo, eje_X, eje_Y, eje_Z) VALUES ('" + id + "', " + str(
            time) + ', ' + str(axis_X) + ', ' + str(axis_Y) + ', ' + str(axis_Z) + ');'
        cursor.execute(query)
        conn.commit()
    #    print(query)
    except:
        print('Insert value error: ' + str(id) + str(time) + str(axis_X) + str(axis_Y) + str(axis_Z))
        conn.rollback()


class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonOpen.clicked.connect(self.open_file)
        self.ui.pushButtonIniciar.clicked.connect(self.initiator_button)
        self.ui.pushButtonDetener.clicked.connect(self.detention_button)
        self.ui.pushButtonServer.clicked.connect(self.sql_server_start)
        self.UDP_PORT = 8888
        self.ui.spinBoxFrecuencia.setValue(100)
        self.IP_list = []
        self.port_list = []
        self.name_list = []
        self.table_set()
        self.project_list = ['testdb']
        self.ui.comboBoxProjects.addItems(self.project_list)
        self.listener_thread_list = []
        self.ServerData = sql_server.ServerData()
        self.ui.tableWidget.setColumnCount(4)
        self.time_interval_start_stop = 3600 # En segundos
        # self.timer = threading.Timer(self.time_interval_start_stop, self.trigger_stop_start)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.trigger_stop_start)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               'Close',
                                               "Do you really want to exit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.detention()
            event.accept()
        else:
            event.ignore()

    def table_set(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(['IP', 'Port', 'Name', 'Status'])
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 25)
        self.ui.tableWidget.setColumnWidth(2, 60)
        self.ui.tableWidget.setColumnWidth(3, 25)

    def add_table_info(self):
        self.ui.tableWidget.clear()
        self.table_set()
        for iterator in range(len(self.IP_list)):
            self.ui.tableWidget.insertRow(iterator)
            self.ui.tableWidget.setItem(iterator, 0, QtWidgets.QTableWidgetItem(self.IP_list[iterator]))
            self.ui.tableWidget.setItem(iterator, 1, QtWidgets.QTableWidgetItem(self.port_list[iterator]))
            self.ui.tableWidget.setItem(iterator, 2, QtWidgets.QTableWidgetItem(self.name_list[iterator]))
            self.ui.tableWidget.setItem(iterator, 3, QtWidgets.QTableWidgetItem('Off'))

    def initiator(self):
        self.ui.pushButtonOpen.setEnabled(False)
        self.initiator_sender()
        self.initiator_listener()

    def detention(self):
        self.detention_sender()
        self.ui.pushButtonIniciar.setEnabled(False)
        self.detention_listener()

    def initiator_button(self):
        self.initiator()
        self.timer.start(self.time_interval_start_stop*1000)

    def detention_button(self):
        self.detention()
        self.timer.stop()

    def initiator_sender(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        freq = int(self.ui.spinBoxFrecuencia.text())
        self.ui.textEditStatus.append('Synchronizing time')
        time_value = obtain_time()
        payload = 'Turn on - '
        payload += str(time_value)
        payload += ' '
        payload += str(freq)
        for IP in self.IP_list:
            sock.sendto(bytes(payload, "utf-8"), (IP, self.UDP_PORT))
        self.ui.textEditStatus.append("Time: " + str(time_value))
        self.ui.textEditStatus.append("Frequency: " + str(freq))
        self.ui.textEditStatus.append("Message sent")
        sock.close()
        print('sock closed')

    def initiator_listener(self):
        self.ui.labelListener.setText('Initiating Threads')
        for ace in range(len(self.IP_list)):
            listener_thread = ListenerThread()
            listener_thread.project = self.ui.comboBoxProjects.currentText()
            listener_thread.status = self.ui.labelListener
            listener_thread.ip = self.IP_list[ace]
            listener_thread.table = self.ui.tableWidget
            listener_thread.name = self.name_list[ace]
            listener_thread.port = int(self.port_list[ace])
            listener_thread.ServerData = self.ServerData
            listener_thread.index = ace
            if self.ui.checkBoxListenerSave.isChecked():
                listener_thread.save_to_file = True
            else:
                listener_thread.save_to_file = False
            if self.ui.checkBoxListenerSQL.isChecked():
                listener_thread.save_to_db = True
            else:
                listener_thread.save_to_db = False
            listener_thread.start()
            self.listener_thread_list.append(listener_thread)

    def detention_sender(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = 'Turn off'
        for IP in self.IP_list:
            sock.sendto(bytes(payload, "utf-8"), (IP, self.UDP_PORT))
        self.ui.textEditStatus.append("Message: " + payload)
        sock.close()

    def detention_listener(self):
        try:
            for ace in range(len(self.IP_list)):
                self.listener_thread_list[ace].kill()
            self.ui.labelListener.setText('Threads killed')
        except:
            print('Error closing listeners')
        self.listener_thread_list = []

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open accelerometer list", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            self.IP_list.clear()
            self.port_list.clear()
            self.name_list.clear()
            self.ui.textEditStatus.append('Opened: \n' + fileName)
            with open(fileName, 'r') as reader:
                for line in reader:
                    IP, port, name = line.split(':')
                    name = name.rstrip('\n')
                    self.IP_list.append(IP)
                    self.port_list.append(port)
                    self.name_list.append(name)
        self.ui.pushButtonDetener.setEnabled(True)
        self.ui.pushButtonIniciar.setEnabled(True)
        self.add_table_info()

    def sql_server_start(self):
        dialog = sql_server.MyDataBaseDialog(user='main', host='10.42.0.157', parent=self)
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            self.ServerData = dialog.ServerData
        self.ui.checkBoxListenerSQL.setEnabled(True)
        self.ui.checkBoxListenerSQL.setChecked(True)

    def trigger_stop_start(self):
        self.detention()
        self.initiator()


class ListenerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._kill = threading.Event()
        self.project = ''
        self.status = QtWidgets.QLabel()
        self.table = QtWidgets.QTableWidget()
        self.ip = ''
        self.port = 8888
        self.name = ''
        self.save_to_db = True
        self.save_to_file = True
        self.ServerData = sql_server.ServerData()
        self.index = 0

    def run(self):
        print('sock opened listener')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self.port))
        table = 'accelerometers_data'
        if self.save_to_file:
            filepath = 'C:\\Users\\pablo\\Documents\\Girona\\OPENARMS\\'
            filename = self.project + '-' + self.name + '-' + str(int(time.time())) + '.csv'
            file = open(filepath + filename, 'a+')
            print(filepath + filename)
        if self.save_to_db:
            # fig = plt.figure()
            # ax1 = fig.add_subplot(1, 1, 1)
            # fig2 = plt.figure()
            # gx1 = fig2.add_subplot(1, 1, 1)
            # lvplt.animation_6axis(filepath + filename, fig, ax1, gx1)
            # plt.show()
            # self.ServerData.set_project(self.project)
            # self.ServerData.connect()
            print(filepath + filename)

        while True:
            data, addr = sock.recvfrom(1024)
            print(data)
            values = data.decode('utf-8').split(sep=',')
            # print(values)
            try:
                if values[0] == 'On':
                    self.table.setItem(self.index, 3, QtWidgets.QTableWidgetItem('On'))
                    self.status.setText(self.name + ' - Turned On')
                elif values[0] == 'Off':
                    self.table.setItem(self.index, 3, QtWidgets.QTableWidgetItem('Off'))
                    self.status.setText(self.name + ' - Turned Off')
                else:
                    n_values = (len(values) - 1) / 7
                    for i_data in range(int(n_values)):
                        time_stamp = float(values[0]) + float(values[i_data * 7 + 1]) / 1000.0
                        text_line = (self.name + ',' + str(time_stamp) + ',' + str(
                            values[i_data * 7 + 2]) + ',' + str(
                            values[i_data * 7 + 3]) + ',' + str(values[i_data * 7 + 4]) + ',' + str(
                            values[i_data * 7 + 5]) + ',' + str(values[i_data * 7 + 6]) + ',' +
                            str(values[i_data * 7 + 7]) + '\n')
                        # print(text_line)
                        # self.status.setText(text_line)
                        if self.save_to_file:
                            file.write(text_line)
                        if self.save_to_db:
                            insert_value(self.ServerData.cursor, self.ServerData.conn, self.name,
                                         time_stamp, values[i_data * 4 + 2], values[i_data * 4 + 3],
                                         values[i_data * 4 + 4], table)
            except ValueError:
                self.status.setText('Error receiving message' + str(values[0]))
            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(0.000001)
            if is_killed:
                sock.close()
                if self.save_to_file:
                    file.close()
                if self.save_to_db:
                    self.ServerData.disconnect()
                break

    def kill(self):
        self._kill.set()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
