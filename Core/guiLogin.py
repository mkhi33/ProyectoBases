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
from Core.DBManager import *
from Core.user import User


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

        
        #instancias de otros TDA'S

        self.DBManager = DBManager()

        self.updateTable()
        
        
        # Eventos de componentes
        self.uiLogin.btnLogin.clicked.connect(self.login)
        
        self.uiMainAdmin.uiMainAdmin.btnManageUsr.clicked.connect(self.openWindowAdminUsr)
        self.uiMainAdmin.uiMainAdmin.btnManageDraw.clicked.connect(self.openWindowDraw)
        self.uiMainAdmin.uiMainAdmin.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainAdmin.uiMainAdmin.btnExit.clicked.connect(self.openDialogExit)

        self.uiMainOp.uiMainOp.btnDraw.clicked.connect(self.openWindowDraw)
        self.uiMainOp.uiMainOp.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainOp.uiMainOp.btnExit.clicked.connect(self.openDialogExit)

        self.uiQuestion.GuiDialogQuestion.btnYes.clicked.connect(self.runAction)
        self.uiQuestion.GuiDialogQuestion.btnNo.clicked.connect(self.closeDialogQuestion)

        self.uiDraw.uiDraw.btnOpeNewDraw.clicked.connect(self.openTkinterDraw)

        self.uiAdmin.uiAdmin.btnSaveUser.clicked.connect(self.registryByAdm)

    def login(self):
        if(self.uiLogin.rbtAdministrador.isChecked()):
            user = self.uiLogin.txtUser.text()
            password = self.uiLogin.txtPassword.text()
            if(self.DBManager.login(user, password, 'Administrador')):
                self.openMainWindowAdmin()
                self.hide()
            else:
                self.uiNotification.uiNotification.lblQuestion.setText("Error al autenticar")
                self.uiNotification.show()
        else:
            self.openMainWindowOp()
            self.hide()

    def registryByAdm(self):
        name = self.uiAdmin.uiAdmin.txtName.text()
        lastName = self.uiAdmin.uiAdmin.txtLastName.text()
        email = self.uiAdmin.uiAdmin.txtEmail.text()
        password = self.uiAdmin.uiAdmin.txtAdmPasword.text()
        userName = self.uiAdmin.uiAdmin.txtUserName.text()
        gender = ""
        if(self.uiAdmin.uiAdmin.rbtFmale.isChecked()):
            gender = 'F'
        elif(self.uiAdmin.uiAdmin.rbtMale.isChecked()):
            gender = 'F'
        # Hay que validar Cuando el usuario no ha seleccionado un genero.
        userType = ""
        if(self.uiAdmin.uiAdmin.rbtAdmi.isChecked()):
            userType = "Administrador"
        elif(self.uiAdmin.uiAdmin.rbtOpe.isChecked()):
            userType = "Administrador"

        year = self.uiAdmin.uiAdmin.dteDate.date().year()
        day = self.uiAdmin.uiAdmin.dteDate.date().day()
        month = self.uiAdmin.uiAdmin.dteDate.date().month()
        birthDate = "%s-%s-%s"%(year, month, day)
        print(birthDate)
        user = User(name, lastName, email, password, userName, gender, userType, birthDate)
        self.DBManager.registry(user)
        self.updateTable()





    def openTkinterDraw(self):
        root = tkinter.Tk()
        drawingApp = DrawingApplication(root)
        drawingApp.mainloop()

    def openMainWindowOp(self):
        self.uiDraw.uiDraw.chkMyDraw.setVisible(False)
        self.uiDraw.uiDraw.lblHeader.setText("Operador")
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
            self.uiMainAdmin.close()
            self.show()
            self.action = ""
        
    def openMainWindowAdmin(self):
        self.uiDraw.uiDraw.chkMyDraw.setVisible(True)
        self.uiDraw.uiDraw.lblHeader.setText("Administrador")
        self.uiMainAdmin.show()
    
    def openWindowAdminUsr(self):
        self.updateTable()
        self.uiAdmin.show()
    def updateTable(self):
        users = self.DBManager.getUsers()
        print(users)
        self.uiAdmin.updateTable(users)

        

