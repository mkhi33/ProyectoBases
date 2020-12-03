#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowMainAdmi import Ui_MainWindow


class GUIMainAdmin(QMainWindow):
    def __init__(self, parent = None):

        super(GUIMainAdmin, self).__init__(parent)
        self.uiMainAdmin = Ui_MainWindow()
        self.uiMainAdmin.setupUi(self)
