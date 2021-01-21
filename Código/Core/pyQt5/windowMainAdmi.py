# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiMainAdm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnManageDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnManageDraw.setGeometry(QtCore.QRect(90, 90, 301, 41))
        self.btnManageDraw.setStyleSheet("QPushButton#btnManageDraw{\n"
"          border-radius: 15px;\n"
"          background-color: #E52462;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnManageDraw:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"}\n"
"")
        self.btnManageDraw.setObjectName("btnManageDraw")
        self.btnManageUsr = QtWidgets.QPushButton(self.centralwidget)
        self.btnManageUsr.setGeometry(QtCore.QRect(90, 150, 301, 41))
        self.btnManageUsr.setStyleSheet("QPushButton#btnManageUsr{\n"
"          border-radius: 15px;\n"
"          background-color: #02735F;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnManageUsr:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"}\n"
"")
        self.btnManageUsr.setObjectName("btnManageUsr")
        self.lblHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(0, 0, 441, 41))
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
        self.btnViewBinnacle = QtWidgets.QPushButton(self.centralwidget)
        self.btnViewBinnacle.setGeometry(QtCore.QRect(90, 210, 301, 41))
        self.btnViewBinnacle.setStyleSheet("QPushButton#btnViewBinnacle{\n"
"          border-radius: 15px;\n"
"          background-color: #8A8824;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnViewBinnacle:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"}\n"
"")
        self.btnViewBinnacle.setObjectName("btnViewBinnacle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 51, 31))
        self.label.setStyleSheet("image: url(:/src/recursos/logo_draw.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 61, 41))
        self.label_2.setStyleSheet("image: url(:/src/recursos/configuracion.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 61, 41))
        self.label_3.setStyleSheet("image: url(:/src/recursos/bitacoras.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(90, 290, 301, 41))
        self.btnExit.setStyleSheet("QPushButton#btnExit{\n"
"          border-radius: 15px;\n"
"          background-color: #000000;\n"
"         border: none;\n"
"         color: #FFFFFF;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnExit:hover {\n"
"    background-color: rgb(22, 184, 39);\n"
"}\n"
"")
        self.btnExit.setObjectName("btnExit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 61, 41))
        self.label_4.setStyleSheet("image: url(:/src/recursos/salida.png);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Administrador"))
        self.btnManageDraw.setText(_translate("MainWindow", "Gestor de dibujos"))
        self.btnManageUsr.setText(_translate("MainWindow", "Gestor de usuarios"))
        self.lblHeader.setText(_translate("MainWindow", "Administrador"))
        self.btnViewBinnacle.setText(_translate("MainWindow", "Ver Bitacora"))
        self.btnExit.setText(_translate("MainWindow", "Salir"))

#import resource_rc
