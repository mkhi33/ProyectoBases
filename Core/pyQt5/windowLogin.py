# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiLogin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUser = QtWidgets.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(250, 70, 151, 121))
        self.lblUser.setStyleSheet("image: url(:/src/recursos/avatar.png);")
        self.lblUser.setText("")
        self.lblUser.setObjectName("lblUser")
        self.lblTextLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblTextLogin.setGeometry(QtCore.QRect(210, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Kalimati")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblTextLogin.setFont(font)
        self.lblTextLogin.setStyleSheet("QLabel#lblTextLogin {\n"
"    font-size:30px;\n"
"}")
        self.lblTextLogin.setObjectName("lblTextLogin")
        self.lblTxtUser = QtWidgets.QLabel(self.centralwidget)
        self.lblTxtUser.setGeometry(QtCore.QRect(150, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblTxtUser.setFont(font)
        self.lblTxtUser.setStyleSheet("QLabel#lblTxtUser{\n"
"    font-size:18px;\n"
"}")
        self.lblTxtUser.setObjectName("lblTxtUser")
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(150, 250, 311, 31))
        self.txtUser.setStyleSheet("QLineEdit#txtUser{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}")
        self.txtUser.setText("")
        self.txtUser.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUser.setObjectName("txtUser")
        self.lblTxtUser_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTxtUser_2.setGeometry(QtCore.QRect(150, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblTxtUser_2.setFont(font)
        self.lblTxtUser_2.setStyleSheet("QLabel#lblTxtUser{\n"
"    font-size:18px;\n"
"}")
        self.lblTxtUser_2.setObjectName("lblTxtUser_2")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(150, 330, 311, 31))
        self.txtPassword.setStyleSheet("QLineEdit#txtPassword{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"}")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPassword.setDragEnabled(False)
        self.txtPassword.setObjectName("txtPassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 320, 71, 51))
        self.label.setStyleSheet("image: url(:/src/recursos/password.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 67, 51))
        self.label_2.setStyleSheet("image: url(:/src/recursos/user.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(240, 430, 131, 51))
        self.btnLogin.setStyleSheet("QPushButton#btnLogin{\n"
"          border-radius: 15px;\n"
"          background-color: #f4511e;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnLogin:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.btnLogin.setObjectName("btnLogin")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 390, 333, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtOperador = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtOperador.setObjectName("rbtOperador")
        self.horizontalLayout.addWidget(self.rbtOperador)
        self.rbtAdministrador = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtAdministrador.setObjectName("rbtAdministrador")
        self.horizontalLayout.addWidget(self.rbtAdministrador)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lblTextLogin.setText(_translate("MainWindow", "Inicio de sesión"))
        self.lblTxtUser.setText(_translate("MainWindow", "Usuario:"))
        self.txtUser.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.lblTxtUser_2.setText(_translate("MainWindow", "Contraseña"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.btnLogin.setText(_translate("MainWindow", "Iniciar Sesión"))
        self.rbtOperador.setText(_translate("MainWindow", "Usuario Operador"))
        self.rbtAdministrador.setText(_translate("MainWindow", "Usuario Administrador"))

#import resource_rc
