# -*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowShowImage import Ui_MainWindow


class GuiShowImage(QMainWindow):
    def __init__(self, parent=None):
        super(GuiShowImage, self).__init__(parent)
        self.uiShowImage = Ui_MainWindow()
        self.uiShowImage.setupUi(self)


