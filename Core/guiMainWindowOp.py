#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowMainOpe import Ui_MainWindow


class GuiMainOp(QMainWindow):
    def __init__(self, parent = None):

        super(GuiMainOp, self).__init__(parent)
        self.uiMainOp = Ui_MainWindow()
        self.uiMainOp.setupUi(self)

