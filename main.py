#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import sys
from Core.draw_tkinter import *
from Core.pyQt5 import resource_rc
from Core.guiLogin import GUILogin
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


"""
Este es el script principal, al iniciar se habre la ventana de inicio de sesión que es la ventana que gestiona
todas las demas ventanas.
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GUILogin()
    main.show()
    sys.exit(app.exec_())