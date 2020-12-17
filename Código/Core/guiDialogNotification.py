#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from Core.pyQt5.windowDialogNotification import Ui_Dialog


class GuiDialogNotification(QDialog):
    """
    @name: GuiDialogNotification
    @Description: Esta clase hereda de QMainWindow y gestiona un dialogo de notificación..
    """
    def __init__(self, parent = None):

        super(GuiDialogNotification, self).__init__(parent)
        self.uiNotification = Ui_Dialog()
        self.uiNotification.setupUi(self)
        
        