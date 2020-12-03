# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 101, 101))
        self.label.setStyleSheet("image: url(:/src/recursos/conversacion.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lblQuestion = QtWidgets.QLabel(Dialog)
        self.lblQuestion.setGeometry(QtCore.QRect(30, 140, 321, 51))
        self.lblQuestion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQuestion.setObjectName("lblQuestion")
        self.btnYes = QtWidgets.QPushButton(Dialog)
        self.btnYes.setGeometry(QtCore.QRect(90, 210, 89, 25))
        self.btnYes.setObjectName("btnYes")
        self.btnNo = QtWidgets.QPushButton(Dialog)
        self.btnNo.setGeometry(QtCore.QRect(210, 210, 89, 25))
        self.btnNo.setObjectName("btnNo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmación"))
        self.lblQuestion.setText(_translate("Dialog", "¿Pregunta de confirmación?"))
        self.btnYes.setText(_translate("Dialog", "Si"))
        self.btnNo.setText(_translate("Dialog", "No"))

#import resource_rc
