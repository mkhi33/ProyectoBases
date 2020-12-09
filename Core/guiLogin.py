#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QColorDialog

from Core.DrawingApplication import DrawingApplication
from Core.pyQt5.windowLogin import Ui_MainWindow
from Core.guiAdmin import GUIAdmin
from Core.guiMainWindowAdmin import GUIMainAdmin
from Core.guiMainWindowOp import GuiMainOp
from Core.guiBinnacle import GuiBinnacle
from Core.guiDraw import GuiDraw
from Core.guiDialogNotification import GuiDialogNotification
from Core.guiDialogQuestion import GuiDialogQuestion
from Core.guiShowImage import GuiShowImage


from Core.draw_tkinter import *
from Core.DBManager import *
from Core.user import User
from datetime import datetime


class GUILogin(QMainWindow):
    def __init__(self, parent = None):

        super(GUILogin, self).__init__(parent)
        self.uiLogin = Ui_MainWindow()
        self.uiLogin.setupUi(self)

        self.action = ""
        self.userPrimaryKey = ""
        self.operation = "save"
        self.idCurrentUser = -1
        self.isAdmin = False
        # Instancias de las ventanas graficas
        self.uiAdmin = GUIAdmin()
        self.uiMainAdmin = GUIMainAdmin()
        self.uiMainOp = GuiMainOp()
        self.uiBinnacle = GuiBinnacle()
        self.uiDraw = GuiDraw()
        self.uiNotification = GuiDialogNotification()
        self.uiQuestion = GuiDialogQuestion()
        self.uiShowImage = GuiShowImage()



        #instancias de otros TDA'S

        self.DBManager = DBManager()

        self.updateTable()
        self.disableEnableFields(False)
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

        self.uiNotification.uiNotification.btnYes.clicked.connect(self.closeDialogNotification)

        self.uiDraw.uiDraw.btnOpeNewDraw.clicked.connect(self.openTkinterDraw)
        self.uiDraw.uiDraw.btnOptEditDraw.clicked.connect(self.editDraw)
        self.uiDraw.uiDraw.btnOpDeleteDraw.clicked.connect(self.openDialogDeleteDraw)
        self.uiDraw.uiDraw.chkMyDraw.clicked.connect(self.eventChek)
        self.uiDraw.uiDraw.btnOpViewDraw.clicked.connect(self.showWindowImage)


        self.uiAdmin.uiAdmin.btnSaveUser.clicked.connect(self.openDialogSaveEdit)
        self.uiAdmin.uiAdmin.btnEditUser.clicked.connect((self.editUser))
        self.uiAdmin.uiAdmin.btnCancel.clicked.connect(self.cancelAction)
        self.uiAdmin.uiAdmin.btnNewUser.clicked.connect(self.createNewUser)
        self.uiAdmin.uiAdmin.btnDeleteUser.clicked.connect(self.openDialogDelete)
        self.uiAdmin.uiAdmin.btnFillColor.clicked.connect(self.setFillColor)
        self.uiAdmin.uiAdmin.btnPenColor.clicked.connect(self.setPenColor)

    def setPenColor(self):
        color = QColorDialog.getColor()
        if(color.isValid()):
            self.DBManager.setPenColor(color.name())
            self.uiAdmin.uiAdmin.txtEditPenColor.setText(color.name())
            self.uiDraw.penColor = color.name()
            self.DBManager.setConfigurationPenColor(self.idCurrentUser, color.name(), self.uiDraw.fillColor)
    def setFillColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.DBManager.setFillColor(color.name())
            self.uiAdmin.uiAdmin.txtEditFillColor.setText(color.name())
            self.uiDraw.fillColor = color.name()
            self.DBManager.setConfigurationPenColor(self.idCurrentUser,self.uiDraw.penColor, color.name())


    def login(self):
        user = self.uiLogin.txtUser.text()
        password = self.uiLogin.txtPassword.text()
        queryUser = "SELECT id FROM User WHERE fk_var_user_name = '%s'"%user
        if(self.uiLogin.rbtAdministrador.isChecked()):
            if(self.DBManager.login(user, password, 'Administrador')):
                self.idCurrentUser = self.DBManager.engine.select(queryUser)[0][0]
                self.uiDraw.uiDraw.chkMyDraw.setChecked(True)
                self.getConfigColors()
                self.openMainWindowAdmin()
                self.isAdmin = True
                self.DBManager.setLoginRegister(self.idCurrentUser,self.uiDraw.fillColor, self.uiDraw.penColor)
                self.hide()
            else:
                self.uiNotification.uiNotification.btnNo.setVisible(False)
                self.uiNotification.uiNotification.lblQuestion.setText("Error al autenticar")
                self.isAdmin = False

                self.uiNotification.show()
        elif self.uiLogin.rbtOperador.isChecked():
            if (self.DBManager.login(user, password, 'Operador')):
                self.idCurrentUser = self.DBManager.engine.select(queryUser)[0][0]
                self.getConfigColors()
                self.openMainWindowOp()
                self.uiDraw.uiDraw.chkMyDraw.setChecked(True)
                self.DBManager.setLoginRegister(self.idCurrentUser, self.uiDraw.fillColor, self.uiDraw.penColor)
                self.isAdmin = False
                self.hide()
            else:
                self.uiNotification.uiNotification.btnNo.setVisible(False)
                self.uiNotification.uiNotification.lblQuestion.setText("Error al autenticar")
                self.uiNotification.show()
                self.isAdmin = False


    def getConfigColors(self):

        self.uiDraw.penColor = self.DBManager.getPenColor()[0][0]
        self.uiDraw.fillColor = self.DBManager.getFillColor()[0][0]

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
            gender = 'M'
        userType = ""
        if(self.uiAdmin.uiAdmin.rbtAdmi.isChecked()):
            userType = "Administrador"
        elif(self.uiAdmin.uiAdmin.rbtOpe.isChecked()):
            userType = "Operador"

        year = self.uiAdmin.uiAdmin.dteDate.date().year()
        day = self.uiAdmin.uiAdmin.dteDate.date().day()
        month = self.uiAdmin.uiAdmin.dteDate.date().month()
        birthDate = "%s-%s-%s"%(year, month, day)

        user = User(name, lastName, email, password, userName, gender, userType, birthDate)

        if self.operation == "save":

            self.DBManager.registry(user)
        elif self.operation == "edit":

            self.DBManager.updateUser(user, self.userPrimaryKey)
        self.updateTable()
        self.cleanForm()
        self.disableEnableFields(False)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(False)


    def editUser(self):
        self.operation = "edit"
        row = self.uiAdmin.getRowValues()
        self.uiAdmin.uiAdmin.txtUserName.setText(row[1])
        self.uiAdmin.uiAdmin.txtName.setText(row[2])
        self.uiAdmin.uiAdmin.txtLastName.setText(row[3])
        self.uiAdmin.uiAdmin.txtEmail.setText(row[4])
        self.userPrimaryKey = row[1]
        try:
            strDate = row[5].split(" ")[0].split("-")
            date = datetime(int(strDate[0]),int(strDate[1]), int(strDate[2]))
            self.uiAdmin.uiAdmin.dteDate.setDate(date)
        except:
            pass

        if(row[6] == 'F'):
            self.uiAdmin.uiAdmin.rbtFmale.setChecked(True)
        elif row[6] == 'M':
            self.uiAdmin.uiAdmin.rbtMale.setChecked(True)

        if(row[7] == 'Administrador'):
            self.uiAdmin.uiAdmin.rbtAdmi.setChecked(True)
        elif row[7] == 'Operador':
            self.uiAdmin.uiAdmin.rbtOpe.setChecked(True)
        self.uiAdmin.uiAdmin.txtAdmPasword.setText(row[8])

        self.uiAdmin.uiAdmin.btnEditUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(True)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(True)

        self.disableEnableFields(True)


    def createNewUser(self):
        self.action = "save"
        self.cleanForm()
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(True)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(True)
        self.disableEnableFields(True)

    def disableEnableFields(self, value = True):
        self.uiAdmin.uiAdmin.txtName.setEnabled(value)
        self.uiAdmin.uiAdmin.txtEmail.setEnabled(value)
        self.uiAdmin.uiAdmin.txtUserName.setEnabled(value)
        self.uiAdmin.uiAdmin.txtLastName.setEnabled(value)
        self.uiAdmin.uiAdmin.txtAdmPasword.setEnabled(value)
        self.uiAdmin.uiAdmin.rbtOpe.setEnabled(value)
        self.uiAdmin.uiAdmin.rbtMale.setEnabled(value)
        self.uiAdmin.uiAdmin.rbtAdmi.setEnabled(value)
        self.uiAdmin.uiAdmin.rbtFmale.setEnabled(value)


    def deleteUser(self):

        row = self.uiAdmin.getRowValues()
        self.DBManager.delete(row[1])
        self.updateTable()
        self.cleanForm()
        self.uiAdmin.uiAdmin.btnCancel.setVisible(False)

    def setActivateButtons(self, value = True):
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(value)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(value)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(value)

    def cancelAction(self):
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(False)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(False)
        self.disableEnableFields(False)

    def cleanForm(self):
        self.uiAdmin.uiAdmin.txtName.setText("")
        self.uiAdmin.uiAdmin.txtLastName.setText("")
        self.uiAdmin.uiAdmin.txtEmail.setText("")
        self.uiAdmin.uiAdmin.txtUserName.setText("")
        self.uiAdmin.uiAdmin.txtAdmPasword.setText("")
        self.uiAdmin.uiAdmin.dteDate.setDate(datetime(2021,1,1))
        self.uiAdmin.uiAdmin.rbtOpe.setChecked(False)
        self.uiAdmin.uiAdmin.rbtAdmi.setChecked(False)
        self.uiAdmin.uiAdmin.rbtMale.setChecked(False)
        self.uiAdmin.uiAdmin.rbtFmale.setChecked(False)


    def deletDraw(self):
        row = self.uiDraw.getRowValues()
        id = row[0]
        self.DBManager.deleteDraw(id)
        self.updateTableDraws()

    def openDialogDeleteDraw(self):
        self.action = "deleteDraw"
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿ Esta seguro que quiere eliminar este dibujo?")
        self.uiQuestion.show()

    def showWindowImage(self):
        row = self.uiDraw.getRowValues()

        if not None in row:
            id = row[0]
            idUser = row[1]
            self.uiDraw.close()
            draw = self.DBManager.getDraw(id)[0][0]
            drawingApp = DrawingApplication(None, flag = "view",contentDraw= draw, idDraw= id, idUser=idUser)

            drawingApp.master.destroy()



    def editDraw(self):
        row = self.uiDraw.getRowValues()
        if not None in row:
            self.uiDraw.close()
            id = row[0]
            draw = self.DBManager.getDraw(id)[0][0]
            root = tkinter.Tk()
            drawingApp = DrawingApplication(root, "edit", draw, isAdmin=self.isAdmin, penColor= self.uiDraw.penColor, fillColor= self.uiDraw.fillColor)
            if(self.uiDraw.uiDraw.chkMyDraw.isChecked()):
                drawingApp.idUser = self.idCurrentUser
            else:
                drawingApp.idUser = row[1]
            drawingApp.idDraw = id
            drawingApp.mainloop()
            if (drawingApp.reload == 'load'):
                self.uiDraw.uiDraw.btnOpViewDraw.setVisible(False)
                self.uiDraw.uiDraw.btnOpeNewDraw.setVisible(False)
                self.uiDraw.uiDraw.btnOpDeleteDraw.setVisible(False)
                self.uiDraw.uiDraw.btnOptEditDraw.setText("Aceptar")
                self.uiDraw.show()

            if (drawingApp.reload == 'close'):
                self.uiDraw.uiDraw.btnOpViewDraw.setVisible(True)
                self.uiDraw.uiDraw.btnOpeNewDraw.setVisible(True)
                self.uiDraw.uiDraw.btnOpDeleteDraw.setVisible(True)
                self.uiDraw.uiDraw.btnOptEditDraw.setText("Editar")

            if(drawingApp.reload == 'new'):
                self.openTkinterDraw()
            if(drawingApp.reload == 'config' ):
                self.openWindowAdminUsr()



            #drawingApp.signal.connect(self.openWindowDraw())
            #drawingApp.signal.connect(self.openWindowDraw)
        else:
            text = "¡Error!\nNo se a seleccionado ningun elemento"
            self.openDialogNotification(text)

    def eventChek(self):
        if(self.uiDraw.uiDraw.chkMyDraw.isChecked()):
            self.updateTableDraws()
        else:
            self.updateTableAllDraws()


    def openTkinterDraw(self):
        self.uiDraw.close()
        root = tkinter.Tk()
        drawingApp = DrawingApplication(root, flag="save", isAdmin = self.isAdmin, penColor= self.uiDraw.penColor, fillColor= self.uiDraw.fillColor)
        drawingApp.idUser = self.idCurrentUser
        drawingApp.mainloop()

        if (drawingApp.reload == 'load'):
            self.uiDraw.uiDraw.btnOpViewDraw.setVisible(False)
            self.uiDraw.uiDraw.btnOpeNewDraw.setVisible(False)
            self.uiDraw.uiDraw.btnOpDeleteDraw.setVisible(False)
            self.uiDraw.uiDraw.btnOptEditDraw.setText("Aceptar")
            self.uiDraw.show()

        if (drawingApp.reload == 'close'):
            self.uiDraw.uiDraw.btnOpViewDraw.setVisible(True)
            self.uiDraw.uiDraw.btnOpeNewDraw.setVisible(True)
            self.uiDraw.uiDraw.btnOpDeleteDraw.setVisible(True)
            self.uiDraw.uiDraw.btnOptEditDraw.setText("Editar")
        if(drawingApp.reload == 'new'):
            self.openTkinterDraw()
        if(drawingApp.reload == 'config' ):
            self.openWindowAdminUsr()

    def saveDraw(self):
        pass

    def openMainWindowOp(self):
        self.uiDraw.uiDraw.chkMyDraw.setVisible(False)
        self.uiDraw.uiDraw.lblHeader.setText("Operador")
        self.uiMainOp.show()

    def openWindowDraw(self):
        draws = self.DBManager.getDrawing(self.idCurrentUser)
        self.uiDraw.uiDraw.chkMyDraw.setChecked(True)
        self.uiDraw.updateTable(draws)
        self.uiDraw.show()


    def openWindowBinnacle(self):
        self.updateBinnacle()
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

    def openDialogSaveEdit(self):
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea guardar?\nSe registraran los cambios en la base de datos.")
        self.action = "saving"
        self.uiQuestion.show()

    def openDialogNotification(self, text= ""):
        self.uiNotification.uiNotification.lblQuestion.setText(text)
        self.uiNotification.uiNotification.btnNo.setVisible(False)
        self.uiNotification.show()

    def openDialogDelete(self):
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea eliminar este usuario?\nSe eliminara el usuario de la base de datos.")
        self.action = "delete"
        self.uiQuestion.show()

    def runAction(self):
        if self.action == "exit":
            self.closeWindowMainOp()
            self.uiQuestion.close()
            self.uiMainAdmin.close()
            self.show()
            self.action = ""
        elif self.action == "saving":
            self.registryByAdm()
            self.uiQuestion.close()
            self.action = ""
        elif self.action == "delete":
            self.deleteUser()
            self.uiQuestion.close()
            self.action = ""
        elif self.action == "deleteDraw":
            self.deletDraw()
            self.uiDraw.uiDraw.chkMyDraw.setChecked(True)
            self.uiQuestion.close()
            self.action = ""

    def openMainWindowAdmin(self):
        self.uiDraw.uiDraw.chkMyDraw.setVisible(True)
        self.uiDraw.uiDraw.lblHeader.setText("Administrador")
        self.uiMainAdmin.show()

    def openWindowAdminUsr(self):
        self.uiAdmin.uiAdmin.txtEditFillColor.setDisabled(True)
        self.uiAdmin.uiAdmin.txtEditPenColor.setDisabled(True)
        self.updateTable()
        self.uiAdmin.show()
    def updateTable(self):
        users = self.DBManager.getUsers()
        self.uiAdmin.updateTable(users)
    def updateTableDraws(self):
        draws = self.DBManager.getDrawing(self.idCurrentUser)
        self.uiDraw.updateTable(draws)
    def updateTableAllDraws(self):
        draws = self.DBManager.getAllDraws()
        self.uiDraw.updateTable(draws)
    def closeDialogNotification(self):
        self.uiNotification.close()
        self.uiNotification.uiNotification.btnYes.setVisible(True)

    def updateBinnacle(self):
        registries = self.DBManager.getRegistries(self.idCurrentUser)
        self.uiBinnacle.updateTable(registries)
        

