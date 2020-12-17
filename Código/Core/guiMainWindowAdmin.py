#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowMainAdmi import Ui_MainWindow


class GUIMainAdmin(QMainWindow):
    """
    @name: GUIMainAdmin
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana que gestiona la ventana principal.
    """
    def __init__(self, parent = None):

        super(GUIMainAdmin, self).__init__(parent)
        self.uiMainAdmin = Ui_MainWindow()
        self.uiMainAdmin.setupUi(self)
        self.centerWindow()
        
    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())