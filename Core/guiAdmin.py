#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowAdmi import Ui_MainWindow


class GUIAdmin(QMainWindow):
    def __init__(self, parent = None):

        super(GUIAdmin, self).__init__(parent)
        self.uiAdmin = Ui_MainWindow()
        self.uiAdmin.setupUi(self)

        
        
        