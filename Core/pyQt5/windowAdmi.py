# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiAdmi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(0, 0, 941, 41))
        font = QtGui.QFont()
        font.setFamily("Saab")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setStyleSheet("background-color: rgb(92, 53, 102);\n"
"color: white;\n"
"")
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName("lblHeader")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(170, 80, 271, 31))
        self.txtName.setStyleSheet("QLineEdit#txtName{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}")
        self.txtName.setAlignment(QtCore.Qt.AlignCenter)
        self.txtName.setObjectName("txtName")
        self.txtLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLastName.setGeometry(QtCore.QRect(500, 80, 271, 31))
        self.txtLastName.setStyleSheet("QLineEdit#txtLastName{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}")
        self.txtLastName.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLastName.setObjectName("txtLastName")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(170, 140, 271, 31))
        self.txtEmail.setStyleSheet("QLineEdit#txtEmail{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}")
        self.txtEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.txtEmail.setObjectName("txtEmail")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 101))
        self.label.setStyleSheet("image: url(:/src/recursos/avatar.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 81, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 60, 91, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 171, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dteDate = QtWidgets.QDateEdit(self.centralwidget)
        self.dteDate.setGeometry(QtCore.QRect(490, 210, 110, 26))
        self.dteDate.setObjectName("dteDate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 190, 191, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 300, 911, 171))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 911, 31))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 200, 96, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbtFmale = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtFmale.setObjectName("rbtFmale")
        self.verticalLayout.addWidget(self.rbtFmale)
        self.rbtMale = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtMale.setObjectName("rbtMale")
        self.verticalLayout.addWidget(self.rbtMale)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 180, 81, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 180, 151, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btnNewUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnNewUser.setGeometry(QtCore.QRect(270, 500, 89, 41))
        self.btnNewUser.setStyleSheet("QPushButton#btnNewUser{\n"
"          border-radius: 15px;\n"
"          background-color: #E4E108;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnNewUser:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.btnNewUser.setObjectName("btnNewUser")
        self.btnEditUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditUser.setGeometry(QtCore.QRect(410, 500, 89, 41))
        self.btnEditUser.setStyleSheet("QPushButton#btnEditUser{\n"
"          border-radius: 15px;\n"
"          background-color: #40CAAF;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnEditUser:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.btnEditUser.setObjectName("btnEditUser")
        self.btnDeleteUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteUser.setGeometry(QtCore.QRect(540, 500, 89, 41))
        self.btnDeleteUser.setStyleSheet("QPushButton#btnDeleteUser{\n"
"          border-radius: 15px;\n"
"          background-color: #f4511e;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnDeleteUser:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.btnDeleteUser.setObjectName("btnDeleteUser")
        self.btnSaveUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveUser.setGeometry(QtCore.QRect(670, 500, 89, 41))
        self.btnSaveUser.setStyleSheet("QPushButton#btnSaveUser{\n"
"          border-radius: 15px;\n"
"          background-color: #15FF03;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnSaveUser:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.btnSaveUser.setObjectName("btnSaveUser")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 200, 125, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbtAdmi = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbtAdmi.setObjectName("rbtAdmi")
        self.verticalLayout_2.addWidget(self.rbtAdmi)
        self.rbtOpe = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbtOpe.setObjectName("rbtOpe")
        self.verticalLayout_2.addWidget(self.rbtOpe)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(500, 120, 191, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtAdmPasword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAdmPasword.setGeometry(QtCore.QRect(490, 140, 271, 31))
        self.txtAdmPasword.setStyleSheet("QLineEdit#txtAdmPasword{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}")
        self.txtAdmPasword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtAdmPasword.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAdmPasword.setObjectName("txtAdmPasword")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestor de usuarios"))
        self.lblHeader.setText(_translate("MainWindow", "Gestionar Usuarios"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.txtLastName.setPlaceholderText(_translate("MainWindow", "Apellido"))
        self.txtEmail.setPlaceholderText(_translate("MainWindow", "Correo Electrónico"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_4.setText(_translate("MainWindow", "Apellido:"))
        self.label_3.setText(_translate("MainWindow", "Correo Electrónico:"))
        self.label_5.setText(_translate("MainWindow", "Fecha de nacimiento: "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "e-mail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha de nacimiento"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Genero"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tipo de usuario"))
        self.label_6.setText(_translate("MainWindow", "Usuarios registrados"))
        self.rbtFmale.setText(_translate("MainWindow", "Femenino"))
        self.rbtMale.setText(_translate("MainWindow", "Masculino"))
        self.label_7.setText(_translate("MainWindow", "Genero:"))
        self.label_8.setText(_translate("MainWindow", "Tipo de usuario:"))
        self.btnNewUser.setText(_translate("MainWindow", "Nuevo"))
        self.btnEditUser.setText(_translate("MainWindow", "Editar"))
        self.btnDeleteUser.setText(_translate("MainWindow", "Eliminar"))
        self.btnSaveUser.setText(_translate("MainWindow", "Guardar"))
        self.rbtAdmi.setText(_translate("MainWindow", "Administrador"))
        self.rbtOpe.setText(_translate("MainWindow", "Operador"))
        self.label_9.setText(_translate("MainWindow", "Contraseña:"))
        self.txtAdmPasword.setPlaceholderText(_translate("MainWindow", "Contraseña"))

#import resource_rc
