#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowDraw import Ui_MainWindow


class GuiDraw(QMainWindow):
    def __init__(self, parent = None):

        super(GuiDraw, self).__init__(parent)
        self.uiDraw = Ui_MainWindow()
        self.uiDraw.setupUi(self)
        