#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowLogin import Ui_MainWindow
from Core.guiAdmin import GUIAdmin
from Core.guiMainWindowAdmin import GUIMainAdmin
from Core.guiMainWindowOp import GuiMainOp
from Core.guiBinnacle import GuiBinnacle
from Core.guiDraw import GuiDraw
from Core.guiDialogNotification import GuiDialogNotification
from Core.guiDialogQuestion import GuiDialogQuestion 

from Core.draw_tkinter import *


class GUILogin(QMainWindow):
    def __init__(self, parent = None):

        super(GUILogin, self).__init__(parent)
        self.uiLogin = Ui_MainWindow()
        self.uiLogin.setupUi(self)

        self.action = ""
        
        
        # Instancias de las ventanas graficas
        self.uiAdmin = GUIAdmin()
        self.uiMainAdmin = GUIMainAdmin()
        self.uiMainOp = GuiMainOp()
        self.uiBinnacle = GuiBinnacle() 
        self.uiDraw = GuiDraw()
        self.uiNotification = GuiDialogNotification()
        self.uiQuestion = GuiDialogQuestion()

        

        
        # Eventos de componentes
        self.uiLogin.btnLogin.clicked.connect(self.login)
        
        self.uiMainAdmin.uiMainAdmin.btnManageUsr.clicked.connect(self.openWindowAdminUsr)
        self.uiMainAdmin.uiMainAdmin.btnManageDraw.clicked.connect(self.openWindowDraw)
        self.uiMainAdmin.uiMainAdmin.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainAdmin.uiMainAdmin.btnExit.clicked.connect(self.closeWindowMainAdmin)

        self.uiMainOp.uiMainOp.btnDraw.clicked.connect(self.openWindowDraw)
        self.uiMainOp.uiMainOp.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainOp.uiMainOp.btnExit.clicked.connect(self.openDialogExit)

        self.uiQuestion.GuiDialogQuestion.btnYes.clicked.connect(self.runAction)
        self.uiQuestion.GuiDialogQuestion.btnNo.clicked.connect(self.closeDialogQuestion)

        self.uiDraw.uiDraw.btnOpeNewDraw.clicked.connect(self.openTkinterDraw)

    def login(self):
        if(self.uiLogin.rbtAdministrador.isChecked()):
            self.openMainWindowAdmin()
            self.hide()
            print("Es Administrador")
        else:
            self.openMainWindowOp()
            self.hide()
            
            print("Es Operador")


    def openTkinterDraw(self):
        root = tkinter.Tk()
        drawingApp = DrawingApplication(root)
        drawingApp.mainloop()

    def openMainWindowOp(self):
        self.uiMainOp.show()

    def openWindowDraw(self):
        self.uiDraw.show()
    def openWindowBinnacle(self):
        self.uiBinnacle.show()   
    def closeWindowMainAdmin(self):
        self.uiMainAdmin.close()
    def closeWindowMainOp(self):
        self.uiMainOp.close()
    def closeDialogQuestion(self):
        self.uiQuestion.close()
        self.action = ""

    def openDialogExit(self):
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea salir?\nSe cerrara su sesión actual.")
        self.action = "exit"
        self.uiQuestion.show()
    def openDialogQuestion(self):
        self.uiQuestion.GuiDialogQuestion.close()

    def runAction(self):
        if self.action == "exit":
            self.closeWindowMainOp()
            self.uiQuestion.close()
            self.show()
            self.action = ""


    def openMainWindowAdmin(self):
        self.uiMainAdmin.show()
    
    def openWindowAdminUsr(self):
        self.uiAdmin.show()
        

