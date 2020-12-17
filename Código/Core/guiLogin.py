#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

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


from Core.draw_tkinter import *
from Core.DBManager import *
from Core.user import User
from datetime import datetime


class GUILogin(QMainWindow):
    """
    @name: GUILogin
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana Login, se tomara esta ventana como ventana principal del código.
    """
    def __init__(self, parent = None):
        """
        @name __init__
        @param parent: QMainWindow
        @description: Clase que gestiona un Login de usuarios.
        """
        super(GUILogin, self).__init__(parent)
        # Se crea las instancias de la ventana Login
        self.uiLogin = Ui_MainWindow()
        self.uiLogin.setupUi(self)
        self.centerWindow()

        #Se crean banderas que indican la acción que ejecuta un usuario.
        self.action = ""
        self.userPrimaryKey = ""
        self.operation = "save"
        self.idCurrentUser = -1
        self.isAdmin = False

        # Instancias de las ventanas gráficas
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
        self.disableEnableFields(False)

        #Eventos click de boton la ventana login
        self.uiLogin.btnLogin.clicked.connect(self.login)

        #Eventos click de los botones de la ventana principal de administrador
        self.uiMainAdmin.uiMainAdmin.btnManageUsr.clicked.connect(self.openWindowAdminUsr)
        self.uiMainAdmin.uiMainAdmin.btnManageDraw.clicked.connect(self.openWindowDraw)
        self.uiMainAdmin.uiMainAdmin.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainAdmin.uiMainAdmin.btnExit.clicked.connect(self.openDialogExit)

        #Eventos click de los botones de la ventana principal del usuario operador
        self.uiMainOp.uiMainOp.btnDraw.clicked.connect(self.openWindowDraw)
        self.uiMainOp.uiMainOp.btnViewBinnacle.clicked.connect(self.openWindowBinnacle)
        self.uiMainOp.uiMainOp.btnExit.clicked.connect(self.openDialogExit)
        #Eventos click de las ventanas de dialogo
        self.uiQuestion.GuiDialogQuestion.btnYes.clicked.connect(self.runAction)
        self.uiQuestion.GuiDialogQuestion.btnNo.clicked.connect(self.closeDialogQuestion)
        self.uiNotification.uiNotification.btnYes.clicked.connect(self.closeDialogNotification)

        #Eventos click de la ventana Draw
        self.uiDraw.uiDraw.btnOpeNewDraw.clicked.connect(self.openTkinterDraw)
        self.uiDraw.uiDraw.btnOptEditDraw.clicked.connect(self.editDraw)
        self.uiDraw.uiDraw.btnOpDeleteDraw.clicked.connect(self.openDialogDeleteDraw)
        self.uiDraw.uiDraw.chkMyDraw.clicked.connect(self.eventChek)
        self.uiDraw.uiDraw.btnOpViewDraw.clicked.connect(self.showWindowImage)

        #Evento click de la ventana administrador de usuarios
        self.uiAdmin.uiAdmin.btnSaveUser.clicked.connect(self.openDialogSaveEdit)
        self.uiAdmin.uiAdmin.btnEditUser.clicked.connect((self.editUser))
        self.uiAdmin.uiAdmin.btnCancel.clicked.connect(self.cancelAction)
        self.uiAdmin.uiAdmin.btnNewUser.clicked.connect(self.createNewUser)
        self.uiAdmin.uiAdmin.btnDeleteUser.clicked.connect(self.openDialogDelete)
        self.uiAdmin.uiAdmin.btnFillColor.clicked.connect(self.setFillColor)
        self.uiAdmin.uiAdmin.btnPenColor.clicked.connect(self.setPenColor)

    def setPenColor(self):
        """
        @name: setPenColor
        @param: No recibe parametros
        @description: Mediante un dialogo de Asigna valor de pencolor en la base de datos.
        @return: No retorna
        """
        color = QColorDialog.getColor()
        if(color.isValid()):
            self.DBManager.setPenColor(color.name())
            self.uiAdmin.uiAdmin.txtEditPenColor.setText(color.name())
            self.uiDraw.penColor = color.name()
            self.DBManager.setConfigurationPenColor(self.idCurrentUser, color.name(), self.uiDraw.fillColor)
    def setFillColor(self):
        """
        @name: setFillColor
        @param: No recibe parametros
        @description: Mediante un dialogo de Asigna valor de FillColor en la base de datos.
        @return: No retorna
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.DBManager.setFillColor(color.name())
            self.uiAdmin.uiAdmin.txtEditFillColor.setText(color.name())
            self.uiDraw.fillColor = color.name()
            self.DBManager.setConfigurationPenColor(self.idCurrentUser,self.uiDraw.penColor, color.name())


    def login(self):
        """
        @name: login
        @param: No recibe parametros
        @description: Obtiene la contraseña y el nombre de usuario de los txtbox y comprueba si son validos para iniciar sesión segun sus credenciales (Administrador u operador), permite el acceso al menu principal en caso de que las credenciales sean correctasa.
        @return No retorna.
        """
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
        """
        @name: getConfigColors
        @param: No recibe parametros
        @description Obtiene los colore pencolor y fillcolor desde la base de datos.
        @return: No retorna.
        """

        self.uiDraw.penColor = self.DBManager.getPenColor()[0][0]
        self.uiDraw.fillColor = self.DBManager.getFillColor()[0][0]

    def registryByAdm(self):
        """
        @name: registryByAdm
        @param: No recibe parametros.
        @description Registra un usuario por el administrador.
                    1. -> Obtiene los datos desde los campos de texto
                    2. -> Crea un objeto usuario
                    3. -> Se manda al manejador de la base de datos para insertarlo en la base de datos.
        @return: No retorna.
        """
        if(self.validateFieldsUsers()):
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
        else:
            self.openDialogNotification("¡Error! \ntodos los campos deben de estar completos.")



    def editUser(self):
        """
        @name:editUser
        @param: No recibe parametros.
        @description: Edita un usuario en particular segun su id.
                        1-> La bandera se asigna en 'edit'
                        2-> Se llenan los campos de texto de la ventana gestor de usuarios con los items de la fila seleccionada.
        @return: No retorna.
        """
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
        self.uiAdmin.uiAdmin.txtAdmPasword.setText("")

        self.uiAdmin.uiAdmin.btnEditUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(True)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(True)

        self.disableEnableFields(True)


    def createNewUser(self):
        """
        @name: createNewUser
        @param: No recibe parametros.
        @description: Responde al evento click del boton crear nuevo usuario de la ventana gestor de usuarios.
        @return: No retorna.
        """
        self.action = "save"
        self.cleanForm()
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(False)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(True)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(True)
        self.disableEnableFields(True)

    def disableEnableFields(self, value = True):
        """
        @name: disableEnableFields
        @param value: Boleano (True o False) para activar/desactivar los campos de la ventana gestor de usuario.
        @description: Desactiva los campos de la ventana de gestor usuario.
        @return No retorna.
        """
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
        """
        @name: deleteUser
        @param: No recibe parametros.
        @description: Elimina un usuario de la base de datos segun un id.
                        -> Esta función responde al evento de confirmación de un dialogo para eliminar usuarios.
        @return: no retorna.
        """

        row = self.uiAdmin.getRowValues()
        self.DBManager.delete(row[1])
        self.updateTable()
        self.cleanForm()
        self.uiAdmin.uiAdmin.btnCancel.setVisible(False)

    def setActivateButtons(self, value = True):
        """
        @name setActivateButtons
        @param value: Booleano(True o False)
        @description: Activa o desactiva los botones de la ventana gestionar usuario.
        @return: No retorna.
        """
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(value)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(value)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(value)

    def cancelAction(self):
        """
        @name: cancelAction
        @param: No recibe parametros.
        @description: Responde al evento cancelar de un dialogo de confirmación, vuelve a activar los botones de la ventana de gestion de usuarios.
        @return: No retorna.
        """
        self.uiAdmin.uiAdmin.btnEditUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnNewUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnDeleteUser.setVisible(True)
        self.uiAdmin.uiAdmin.btnCancel.setVisible(False)
        self.uiAdmin.uiAdmin.btnSaveUser.setVisible(False)
        self.disableEnableFields(False)

    def cleanForm(self):
        """
        @name: cleanForm
        @param: No recibe parametros
        @description: Limpia el formulario de la ventana gestionar usuario.
        @return: No retorna.
        """
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
        """
        @name: deleteDraw
        @param: No recibe parametros
        @description: Elimina un dibujo de la basde de datos segun el dibujo seleccionado en la tabla.
        @return: No retorna.
        """
        row = self.uiDraw.getRowValues()
        id = row[0]
        self.DBManager.deleteDraw(id)
        self.updateTableDraws()

    def openDialogDeleteDraw(self):
        """
        @name: openDialogDeleteDraw
        @param: No recibe parametros.
        @description: Abre un dialogo para confirmar si desea eliminar un dibujo.
        @return: No retorna.
        """
        self.action = "deleteDraw"
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿ Esta seguro que quiere eliminar este dibujo?")
        self.uiQuestion.show()

    def showWindowImage(self):
        """
        @name: showWindowImage
        @param: No recibe parametros
        @description: Abre una ventana para la visualización de dibujo.
        @return: No retorna.
        """
        
        row = self.uiDraw.getRowValues()

        if not None in row:
            id = row[0]
            idUser = row[1]
            self.uiDraw.close()
            draw = self.DBManager.getDraw(id)[0][0]
            drawingApp = DrawingApplication(None, flag = "view",contentDraw= draw, idDraw= id, idUser=idUser)

            drawingApp.master.destroy()



    def editDraw(self):
        """
        @name: editDraw
        @param: No recibe parametros
        @description: Segun el dibujo selelccionado en la tabla que lista todos los dibujos se editara mediante su id y se actualizara en la base de datos.
        @return: No retorna.
        """
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
        else:
            text = "¡Error!\nNo se a seleccionado ningun elemento"
            self.openDialogNotification(text)

    def eventChek(self):
        """
        @name: eventChek
        @param: No recibe parametros.
        @description: Responde al evento click del checkbox de la ventana administrador de usuarios.
        @return: No retorna.
        """
        if(self.uiDraw.uiDraw.chkMyDraw.isChecked()):
            self.updateTableDraws()
        else:
            self.updateTableAllDraws()


    def openTkinterDraw(self):
        """
        @name: openTkinterDraw
        @param: No recibe parametros.
        @description: Abre una ventana Tkinter.
        @return: No retorna.
        """
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


    def openMainWindowOp(self):
        """
        @name: openMainWindowOp
        @param: No recibe parametros
        @description: Abre una ventana principal de usuario operador.
        @return: No retorna
        """
        self.uiDraw.uiDraw.chkMyDraw.setVisible(False)
        self.uiDraw.uiDraw.lblHeader.setText("Operador")
        self.uiMainOp.show()

    def openWindowDraw(self):
        """
        @name: openWindowDraw
        @param: No recibe parametros
        @description: Abre una ventana de gestor de dibujos.
        @return: No retorna.
        """
        draws = self.DBManager.getDrawing(self.idCurrentUser)
        self.uiDraw.uiDraw.chkMyDraw.setChecked(True)
        self.uiDraw.updateTable(draws)
        self.uiDraw.show()


    def openWindowBinnacle(self):
        """
        @name: openWindowBinnacle
        @param: No recibe parametros.
        @description: Abre una ventana de bitacora.
        @return: no retorna.
        """
        self.updateBinnacle()
        self.uiBinnacle.show()
    def closeWindowMainAdmin(self):
        """
        @name: closeWindowMainAdmin.
        @param: No recibe parametros.
        @description: Cierra una ventana principal de usuario administrador.
        @return
        """

        self.uiMainAdmin.close()
    def closeWindowMainOp(self):
        """
        @name: closeWindowMainOp
        @param: No recibe parametros.
        @description: Cierra una ventana principal de usuario operador.
        @return
        """
        self.uiMainOp.close()
    def closeDialogQuestion(self):
        """
        @name: closeDialogQuestion
        @param: No recibe parametros.
        @description: Cierra un dialogo de confirmación.
        @return: No retorna.
        """
        self.uiQuestion.close()
        self.action = ""

    def openDialogExit(self):
        """
        @name: openDialogExit
        @param: No recibe parametros.
        @description: Abre un dialogo de confirmación.
        @return: No retorna.
        """
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea salir?\nSe cerrara su sesión actual.")
        self.action = "exit"
        self.uiQuestion.show()

    def openDialogSaveEdit(self):
        """
        @name:openDialogSaveEdit
        @param: No recibe parametros.
        @description: Abre un dialogo para editar o guardar.
        @return: no retorna.
        """
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea guardar?\nSe registraran los cambios en la base de datos.")
        self.action = "saving"
        self.uiQuestion.show()

    def openDialogNotification(self, text= ""):
        """
        @name: openDialogNotification
        @param text: Texto a mostrar en el dialogo.
        @description: Muestra un dialogo de notificación con un texto preestablecido.
        @return: No retorna.
        """
        self.uiNotification.uiNotification.lblQuestion.setText(text)
        self.uiNotification.uiNotification.btnNo.setVisible(False)
        self.uiNotification.show()

    def openDialogDelete(self):
        """
        @name: openDialogDelete
        @param: No recibe parametros.
        @description: Abre un dialogo de confirmación para la eliminación.
        @return: No retorna.
        """
        self.uiQuestion.GuiDialogQuestion.lblQuestion.setText("¿Desea eliminar este usuario?\nSe eliminara el usuario de la base de datos.")
        self.action = "delete"
        self.uiQuestion.show()

    def runAction(self):
        """
        @name: runAction
        @param: No recibe parametros.
        @description: Segun la bandera 'action'ejecuta una acción. (exit, saving, delete, deleteDraw)
        @return: No retorna.
        """
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
        """
        @name: openMainWindowAdmin
        @param: No recibe parametros.
        @description: Abre la ventana principal de administrador.
        @return
        """
        self.uiDraw.uiDraw.chkMyDraw.setVisible(True)
        self.uiDraw.uiDraw.lblHeader.setText("Administrador")
        self.uiMainAdmin.show()

    def openWindowAdminUsr(self):
        """
        @name: openWindowAdminUsr
        @param: No recibe parametros.
        @description: Abre una ventana de administrador de usuarios.
        @return: No retorna.
        """
        self.uiAdmin.uiAdmin.txtEditFillColor.setDisabled(True)
        self.uiAdmin.uiAdmin.txtEditPenColor.setDisabled(True)
        self.updateTable()
        self.uiAdmin.show()
    def updateTable(self):
        """
        @name: updateTable
        @param: No recibe parametros.
        @description: Actualiza la tabla de la ventana gestion de usuarios.
        @return: No retorna.
        """
        users = self.DBManager.getUsers()
        self.uiAdmin.updateTable(users)
    def updateTableDraws(self):
        """
        @name: updateTableDraws
        @param: No recibe parametros.
        @description: Actualiza la tabla de dibujo segun los dibujos que tenga un usuario en la base de datos.
        @return: No retorna.
        """
        draws = self.DBManager.getDrawing(self.idCurrentUser)
        self.uiDraw.updateTable(draws)
    def updateTableAllDraws(self):
        """
        @name: updateTableAllDraws
        @param: No recibe parametros.
        @description: Actualiza una tabla con todos los dibujos de todos los usuarios.
        @return: No retorna.
        """
        draws = self.DBManager.getAllDraws()
        self.uiDraw.updateTable(draws)
    def closeDialogNotification(self):
        """
        @name: closeDialogNotification.
        @param: No recibe parametros.
        @description: Cierra un dialogo de notificación.
        @return: No retorna.
        """
        self.uiNotification.close()
        self.uiNotification.uiNotification.btnYes.setVisible(True)

    def updateBinnacle(self):
        """
        @name:updateBinnacle.
        @param: No recibe parametros.
        @description: Actualiza la tabla de bitacora segun la actividad del usuario.
        @return: No retorna.
        """
        registries = self.DBManager.getRegistries(self.idCurrentUser)
        self.uiBinnacle.updateTable(registries)

    def validateFieldsUsers(self):
        """
        @name: validateFieldsUsers
        @param: No recibe parametros.
        @description: Valida que los campos de texto no esten vacios al momento de ingresar un nuevo usuario.
        :return: Booleano.
        """
        if(self.uiAdmin.uiAdmin.txtUserName.text() != "" and self.uiAdmin.uiAdmin.txtName.text() != "" and self.uiAdmin.uiAdmin.txtLastName.text() != "" and self.uiAdmin.uiAdmin.txtEmail.text() != "" and self.uiAdmin.uiAdmin.txtAdmPasword.text() != ""):
            return True
        return False
        
    def centerWindow(self):
        """
        @name: centerWindow
        @param: No recibe parametros
        @description: Inicia la ventana en el centro de la pantalla.
        @return: No retorna
        """
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())
