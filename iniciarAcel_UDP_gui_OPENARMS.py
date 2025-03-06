# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/psierra/Dropbox/CIMNE/Suite/ui/iniciarAcel_UDP.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 600)
        Dialog.setMinimumSize(QtCore.QSize(480, 600))
        Dialog.setMaximumSize(QtCore.QSize(480, 600))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 471, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOpen = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(45, 40))
        self.pushButtonOpen.setMaximumSize(QtCore.QSize(45, 40))
        self.pushButtonOpen.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/openfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOpen.setIcon(icon)
        self.pushButtonOpen.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout.addWidget(self.pushButtonOpen)
        self.pushButtonServer = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonServer.setMinimumSize(QtCore.QSize(45, 40))
        self.pushButtonServer.setMaximumSize(QtCore.QSize(45, 40))
        self.pushButtonServer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonServer.setIcon(icon1)
        self.pushButtonServer.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonServer.setObjectName("pushButtonServer")
        self.pushButtonServer.setEnabled(False)
        self.horizontalLayout.addWidget(self.pushButtonServer)
        self.pushButtonIniciar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonIniciar.setEnabled(False)
        self.pushButtonIniciar.setMinimumSize(QtCore.QSize(45, 40))
        self.pushButtonIniciar.setMaximumSize(QtCore.QSize(45, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonIniciar.setFont(font)
        self.pushButtonIniciar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/boton-de-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonIniciar.setIcon(icon2)
        self.pushButtonIniciar.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonIniciar.setObjectName("pushButtonIniciar")
        self.horizontalLayout.addWidget(self.pushButtonIniciar)
        self.pushButtonDetener = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDetener.setEnabled(False)
        self.pushButtonDetener.setMinimumSize(QtCore.QSize(45, 40))
        self.pushButtonDetener.setMaximumSize(QtCore.QSize(45, 40))
        self.pushButtonDetener.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/detener.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDetener.setIcon(icon3)
        self.pushButtonDetener.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonDetener.setObjectName("pushButtonDetener")
        self.horizontalLayout.addWidget(self.pushButtonDetener)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelFrecuencia = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelFrecuencia.setFont(font)
        self.labelFrecuencia.setObjectName("labelFrecuencia")
        self.horizontalLayout_4.addWidget(self.labelFrecuencia)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.spinBoxFrecuencia = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxFrecuencia.setFont(font)
        self.spinBoxFrecuencia.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxFrecuencia.setMinimum(50)
        self.spinBoxFrecuencia.setMaximum(250)
        self.spinBoxFrecuencia.setSingleStep(50)
        self.spinBoxFrecuencia.setProperty("value", 200)
        self.spinBoxFrecuencia.setDisplayIntegerBase(10)
        self.spinBoxFrecuencia.setObjectName("spinBoxFrecuencia")
        self.horizontalLayout_4.addWidget(self.spinBoxFrecuencia)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelProject = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelProject.setFont(font)
        self.labelProject.setObjectName("labelProject")
        self.horizontalLayout_5.addWidget(self.labelProject)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.comboBoxProjects = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxProjects.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxProjects.setObjectName("comboBoxProjects")
        self.horizontalLayout_5.addWidget(self.comboBoxProjects)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBoxListenerSave = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxListenerSave.setChecked(True)
        self.checkBoxListenerSave.setObjectName("checkBoxListenerSave")
        self.horizontalLayout_6.addWidget(self.checkBoxListenerSave)
        self.checkBoxListenerSQL = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxListenerSQL.setEnabled(True)
        self.checkBoxListenerSQL.setCheckable(True)
        self.checkBoxListenerSQL.setChecked(False)
        self.checkBoxListenerSQL.setObjectName("checkBoxListenerSQL")
        self.horizontalLayout_6.addWidget(self.checkBoxListenerSQL)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelAccList = QtWidgets.QLabel(self.layoutWidget)
        self.labelAccList.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelAccList.setFont(font)
        self.labelAccList.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccList.setObjectName("labelAccList")
        self.horizontalLayout_2.addWidget(self.labelAccList)
        self.labelSenderStatus = QtWidgets.QLabel(self.layoutWidget)
        self.labelSenderStatus.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSenderStatus.setFont(font)
        self.labelSenderStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenderStatus.setObjectName("labelSenderStatus")
        self.horizontalLayout_2.addWidget(self.labelSenderStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 1999999))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(57)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.textEditStatus = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEditStatus.setEnabled(True)
        self.textEditStatus.setMaximumSize(QtCore.QSize(16777215, 160000))
        self.textEditStatus.setReadOnly(True)
        self.textEditStatus.setObjectName("textEditStatus")
        self.horizontalLayout_3.addWidget(self.textEditStatus)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.labelListenerTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelListenerTitle.setFont(font)
        self.labelListenerTitle.setObjectName("labelListenerTitle")
        self.verticalLayout.addWidget(self.labelListenerTitle)
        self.labelListener = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelListener.setFont(font)
        self.labelListener.setText("")
        self.labelListener.setObjectName("labelListener")
        self.verticalLayout.addWidget(self.labelListener)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Acc Controller"))
        self.labelFrecuencia.setText(_translate("Dialog", "Frequency Hz"))
        self.labelProject.setText(_translate("Dialog", "Project Name"))
        self.checkBoxListenerSave.setText(_translate("Dialog", "Save in file"))
        self.checkBoxListenerSQL.setText(_translate("Dialog", "Graph"))
        self.labelAccList.setText(_translate("Dialog", "Accelerometer list"))
        self.labelSenderStatus.setText(_translate("Dialog", "Sender Status"))
        self.labelListenerTitle.setText(_translate("Dialog", "Listener Status"))
import iconos_rc
