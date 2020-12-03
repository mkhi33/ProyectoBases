#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowBinnacle import Ui_MainWindow


class GuiBinnacle(QMainWindow):
    def __init__(self, parent = None):

        super(GuiBinnacle, self).__init__(parent)
        self.uiBinnacle = Ui_MainWindow()
        self.uiBinnacle.setupUi(self)
        