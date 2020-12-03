#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from Core.pyQt5.windowDialogNotification import Ui_Dialog


class GuiDialogNotification(QDialog):
    def __init__(self, parent = None):

        super(GuiDialogNotification, self).__init__(parent)
        self.uiNotification = Ui_Dialog()
        self.uiNotification.setupUi(self)
        