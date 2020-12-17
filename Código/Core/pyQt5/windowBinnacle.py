# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiBinnacle.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 801, 31))
        self.label_2.setStyleSheet("background-color: rgb(103, 69, 130);\n"
"color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tblBitacora = QtWidgets.QTableWidget(self.centralwidget)
        self.tblBitacora.setGeometry(QtCore.QRect(0, 70, 801, 351))
        self.tblBitacora.setStyleSheet("")
        self.tblBitacora.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tblBitacora.setRowCount(10)
        self.tblBitacora.setColumnCount(6)
        self.tblBitacora.setObjectName("tblBitacora")
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBitacora.setHorizontalHeaderItem(5, item)
        self.tblBitacora.horizontalHeader().setDefaultSectionSize(130)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro de bitácora"))
        self.label.setText(_translate("MainWindow", "Registros de Bitácora"))
        self.label_2.setText(_translate("MainWindow", "Tabla de registros"))
        item = self.tblBitacora.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Acción"))
        item = self.tblBitacora.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha de registro"))
        item = self.tblBitacora.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre de usuario"))
        item = self.tblBitacora.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dibujo"))
        item = self.tblBitacora.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pen color"))
        item = self.tblBitacora.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fill color"))

