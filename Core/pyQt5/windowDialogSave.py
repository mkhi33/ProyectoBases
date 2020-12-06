# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiDialogSave.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 205)
        Dialog.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.txtFileName = QtWidgets.QLineEdit(Dialog)
        self.txtFileName.setGeometry(QtCore.QRect(50, 70, 281, 31))
        self.txtFileName.setStyleSheet("QLineEdit#txtFileName{\n"
"    border-radius:15px;\n"
"    background-color:#16B89B;\n"
"    text-align:center;\n"
"}\n"
"")
        self.txtFileName.setObjectName("txtFileName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 171, 17))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setGeometry(QtCore.QRect(250, 130, 89, 25))
        self.btnSave.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(140, 130, 89, 25))
        self.btnCancel.setStyleSheet("\n"
"background-color: rgb(238, 238, 236);")
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Guardar como ..."))
        self.label_2.setText(_translate("Dialog", "Guardar como ..."))
        self.btnSave.setText(_translate("Dialog", "Guardar"))
        self.btnCancel.setText(_translate("Dialog", "cancelar"))

