# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiDraw.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(0, 0, 961, 41))
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
        self.tablOptDraw = QtWidgets.QTableWidget(self.centralwidget)
        self.tablOptDraw.setGeometry(QtCore.QRect(40, 161, 871, 191))
        self.tablOptDraw.setRowCount(10)
        self.tablOptDraw.setColumnCount(4)
        self.tablOptDraw.setObjectName("tablOptDraw")
        item = QtWidgets.QTableWidgetItem()
        self.tablOptDraw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablOptDraw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablOptDraw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablOptDraw.setHorizontalHeaderItem(3, item)
        self.tablOptDraw.horizontalHeader().setDefaultSectionSize(200)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 120, 871, 41))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnOpeNewDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpeNewDraw.setGeometry(QtCore.QRect(190, 370, 101, 41))
        self.btnOpeNewDraw.setStyleSheet("QPushButton#btnOpeNewDraw{\n"
"          border-radius: 15px;\n"
"          background-color: rgb(22, 184, 39);\n"
"\n"
"         border: none;\n"
"         color: black;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnOpeNewDraw:hover {\n"
"    background-color: black;\n"
"    cursor:pointer;\n"
"color: white;\n"
"}\n"
"")
        self.btnOpeNewDraw.setObjectName("btnOpeNewDraw")
        self.btnOptEditDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnOptEditDraw.setGeometry(QtCore.QRect(420, 370, 111, 41))
        self.btnOptEditDraw.setStyleSheet("QPushButton#btnOptEditDraw{\n"
"          border-radius: 15px;\n"
"          background-color: rgb(3, 255, 198);\n"
"\n"
"         border: none;\n"
"         color: black;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnOptEditDraw:hover {\n"
"    background-color: black;\n"
"    cursor:pointer;\n"
"color:white;\n"
"}\n"
"")
        self.btnOptEditDraw.setObjectName("btnOptEditDraw")
        self.btnOpDeleteDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpDeleteDraw.setGeometry(QtCore.QRect(560, 370, 121, 41))
        self.btnOpDeleteDraw.setStyleSheet("QPushButton#btnOpDeleteDraw{\n"
"          border-radius: 15px;\n"
"          background-color: rgb(255, 148, 3);\n"
"\n"
"         border: none;\n"
"         color: black;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnOpDeleteDraw:hover {\n"
"    background-color: black;\n"
"    cursor:pointer;\n"
"color: white;\n"
"}\n"
"")
        self.btnOpDeleteDraw.setObjectName("btnOpDeleteDraw")
        self.btnOpViewDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpViewDraw.setGeometry(QtCore.QRect(300, 370, 101, 41))
        self.btnOpViewDraw.setStyleSheet("QPushButton#btnOpViewDraw{\n"
"          border-radius: 15px;\n"
"          background-color: rgb(229, 50, 107);\n"
"\n"
"         border: none;\n"
"         color: black;\n"
"         text-align: center;\n"
"          font-size: 14px;\n"
"          margin: 5px;\n"
"}\n"
"\n"
"QPushButton#btnOpViewDraw:hover {\n"
"    background-color: black;\n"
"    cursor:pointer;\n"
"color: white;\n"
"}\n"
"")
        self.btnOpViewDraw.setObjectName("btnOpViewDraw")
        self.chkMyDraw = QtWidgets.QCheckBox(self.centralwidget)
        self.chkMyDraw.setGeometry(QtCore.QRect(690, 90, 171, 23))
        self.chkMyDraw.setObjectName("chkMyDraw")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dibujos"))
        self.lblHeader.setText(_translate("MainWindow", "Tipo de usuario"))
        item = self.tablOptDraw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tablOptDraw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre del dibujo"))
        item = self.tablOptDraw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha de creación"))
        item = self.tablOptDraw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha de modificación"))
        self.label.setText(_translate("MainWindow", "Dibujos"))
        self.btnOpeNewDraw.setText(_translate("MainWindow", "Nuevo dibujo"))
        self.btnOptEditDraw.setText(_translate("MainWindow", "Editar dibujo"))
        self.btnOpDeleteDraw.setText(_translate("MainWindow", "Eliminar dibujo"))
        self.btnOpViewDraw.setText(_translate("MainWindow", "Ver dibujo"))
        self.chkMyDraw.setText(_translate("MainWindow", "Ver solo mis dibujos"))

