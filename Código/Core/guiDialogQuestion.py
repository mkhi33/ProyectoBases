#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from Core.pyQt5.windowDialogQuestion import Ui_Dialog


class GuiDialogQuestion(QDialog):
    """
    @name: GuiDialogQuestion
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de un dialogo de confirmación.
    """
    def __init__(self, parent = None):

        super(GuiDialogQuestion, self).__init__(parent)
        self.GuiDialogQuestion = Ui_Dialog()
        self.GuiDialogQuestion.setupUi(self)
        
