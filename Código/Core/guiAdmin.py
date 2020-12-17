#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowAdmi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget



class GUIAdmin(QMainWindow):
    """
    @name: GUIAdmin
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana Administrador de usuarios.
    """
    def __init__(self, parent = None):

        super(GUIAdmin, self).__init__(parent)
        self.uiAdmin = Ui_MainWindow()
        self.uiAdmin.setupUi(self)
        self.uiAdmin.btnCancel.setVisible(False)
        self.uiAdmin.btnSaveUser.setVisible(False)
        self.position = (0,0)
        self.centerWindow()




    def setHorizontalHeaderItem(self, size):
        """
        @name: setHorizontalHeaderItem
        @param size: Total de filas que tendra la tabla.
        @description: asigna un espacio a la tabla qt5 para agregar items.
        @return: No retorna.
        """

        for i in range(size):
            self.position = self.uiAdmin.tableWidget.rowCount()
            self.uiAdmin.tableWidget.insertRow(self.position)
            self.uiAdmin.tableWidget.resizeRowsToContents()

    def deleteAllRows(self):
        """
        @name: deleteAllRows
        @param: No recibe parametros
        @description: Elimina todas las filas de una QTableWidget
        @return: No retorna.
        """
        model:QAbstractTableModel = self.uiAdmin.tableWidget.model()
        model.removeRows(0, model.rowCount())
        return True

    def updateTable(self, content = []):
        """
        @name: updateTable
        @param content: Lista de listas que contiene los elementos a agregar a esta tabla.
        @description: Genera la tabla con la nueva actualización de elementos:
                        1-> Elimina el contenido que tenia anteriormente la tabla.
                        2-> Se reserva el nuevo espacio de filas.
                        3-> Se extraen los valores a agregar a la tabla, en formato texto.
                        4-> Se crean los items QTableWidgetItem
                        5-> Se restringe la edición de tablas con setFlags
                        6-> agregamos los items a la tabla con setItems.
        @return: No retorna
        """
        self.deleteAllRows()
        self.setHorizontalHeaderItem(len(content))
        for i in range(len(content)):
            
            id = "%s"%content[i][0]
            userName = "%s"%content[i][1]
            name = "%s"%content[i][2]
            lastName = "%s"%content[i][3]
            email = "%s"%content[i][4]
            birthDate = "%s"%content[i][5]
            gender = "%s" % content[i][6]
            typeUser = "%s" % content[i][7]
            password = "%s" % content[i][8]



            itemId = QTableWidgetItem(id)
            itemUserName = QTableWidgetItem(userName)
            itemName = QTableWidgetItem(name)
            itemLastName = QTableWidgetItem(lastName)
            itemEmail = QTableWidgetItem(email)
            itemBirthDate = QTableWidgetItem(birthDate)
            itemGender = QTableWidgetItem(gender)
            itemTypeUser = QTableWidgetItem(typeUser)
            itemPassword = QTableWidgetItem(password)



            itemId.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemUserName.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemName.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemLastName.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemEmail.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemBirthDate.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemGender.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemTypeUser.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemPassword.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)



            self.uiAdmin.tableWidget.setItem(i,0, itemId)
            self.uiAdmin.tableWidget.setItem(i, 1, itemUserName)
            self.uiAdmin.tableWidget.setItem(i,2,itemName )
            self.uiAdmin.tableWidget.setItem(i,3,itemLastName )
            self.uiAdmin.tableWidget.setItem(i, 4, itemEmail)
            self.uiAdmin.tableWidget.setItem(i,5, itemBirthDate )
            self.uiAdmin.tableWidget.setItem(i,6,itemGender )
            self.uiAdmin.tableWidget.setItem(i,7, itemTypeUser)
            self.uiAdmin.tableWidget.setItem(i,8,itemPassword )



    def getIndexRow(self):
        """
        @name: getIndexRow
        @param: No recibe parametros.
        @description: Obtiene el indice de la fila seleccionada por el usuario.
        @return retorna la fila seleccionada. 
        """

        return self.uiAdmin.tableWidget.currentIndex().row()

    def getRowValues(self):
        """
        @name: getRowValues
        @param: No recibe parametros
        @description: Obtiene la data que tiene cada fila y los agrega a una lista.
        @return: Retorna una lista de lista con los itemss de la tabla.
        """
        indexRow = self.getIndexRow()
        listItems = []
        for i in range(9):
            item = self.uiAdmin.tableWidget.model().index(indexRow, i)
            value = self.uiAdmin.tableWidget.model().data(item)
            listItems.append(value)
        return  listItems


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