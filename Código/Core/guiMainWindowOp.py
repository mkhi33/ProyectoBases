#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowMainOpe import Ui_MainWindow


class GuiMainOp(QMainWindow):
    """
    @name: GuiMainOp
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana principal de usuarios operadores.
    """
    def __init__(self, parent = None):

        super(GuiMainOp, self).__init__(parent)
        self.uiMainOp = Ui_MainWindow()
        self.uiMainOp.setupUi(self)
        self.centerWindow()

    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())