# -*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from Core.pyQt5.windowDialogSave import Ui_Dialog


class GuiDialogSave(QDialog):
    def __init__(self, parent=None):
        super(GuiDialogSave, self).__init__(parent)
        self.uiDialogSave = Ui_Dialog()
        self.uiDialogSave.setupUi(self)

