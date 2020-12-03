#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from from Core.guiLogin import GUILogin


class run(QMainWindow):
    def __init__(self, parent = None):
        super(run, self).__init__(parent)
        self.guiLogin = GUILogin()

