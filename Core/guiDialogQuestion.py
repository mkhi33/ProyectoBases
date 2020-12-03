#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from Core.pyQt5.windowDialogQuestion import Ui_Dialog


class GuiDialogQuestion(QDialog):
    def __init__(self, parent = None):

        super(GuiDialogQuestion, self).__init__(parent)
        self.GuiDialogQuestion = Ui_Dialog()
        self.GuiDialogQuestion.setupUi(self)
        
        