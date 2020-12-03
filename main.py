import sys
from Core.draw_tkinter import *
from Core.pyQt5 import resource_rc
from Core.guiLogin import GUILogin

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit




"""
def main():

    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("Ejecución completada")

if __name__ == "__main__":
    main()
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GUILogin()
    main.show()
    sys.exit(app.exec_())