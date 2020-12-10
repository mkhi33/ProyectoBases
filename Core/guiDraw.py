#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from Core.pyQt5.windowDraw import Ui_MainWindow
from PyQt5.QtCore import Qt, QAbstractTableModel


class GuiDraw(QMainWindow):
    """
    @name: GuiDraw
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana para gestionar dibujos.
    """
    def __init__(self, parent = None):

        super(GuiDraw, self).__init__(parent)
        self.uiDraw = Ui_MainWindow()
        self.uiDraw.setupUi(self)
        self.penColor = '#000000'
        self.fillColor = '#000000'
    def deleteAllRows(self):
        """
        @name: deleteAllRows
        @param: No recibe parametros
        @description: Elimina todas las filas de una QTableWidget
        @return: True.
        """
        model:QAbstractTableModel = self.uiDraw.tablOptDraw.model()
        model.removeRows(0, model.rowCount())
        return True
    def setHorizontalHeaderItem(self, size):
        """
        @name: setHorizontalHeaderItem
        @param size: Total de filas que tendra la tabla.
        @description: asigna un espacio a la tabla qt5 para agregar items.
        @return: No retorna.
        """
        for i in range(size):
            self.position = self.uiDraw.tablOptDraw.rowCount()
            self.uiDraw.tablOptDraw.insertRow(self.position)
            self.uiDraw.tablOptDraw.resizeRowsToContents()

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
            id = str(content[i][0])
            idUser = str(content[i][1])
            txtName = str(content[i][2])
            dateCreation = str(content[i][3])
            timModification = str(content[i][4])
            #jsonFile = str(content[i][5])

            itemId = QTableWidgetItem(id)
            itemIdUser = QTableWidgetItem(idUser)
            itemTxtName = QTableWidgetItem(txtName)
            itemDateCreation = QTableWidgetItem(dateCreation)
            itemModification = QTableWidgetItem(timModification)

            itemId.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemIdUser.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemTxtName.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemDateCreation.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemModification.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.uiDraw.tablOptDraw.setItem(i, 0, itemId)
            self.uiDraw.tablOptDraw.setItem(i, 1, itemIdUser)
            self.uiDraw.tablOptDraw.setItem(i, 2, itemTxtName)
            self.uiDraw.tablOptDraw.setItem(i, 3, itemDateCreation)
            self.uiDraw.tablOptDraw.setItem(i, 4, itemModification)


    def getIndexRow(self):
        """
        @name: getIndexRow
        @param: No recibe parametros.
        @description: Obtiene el indice de la fila seleccionada por el usuario.
        @return retorna la fila seleccionada. 
        """
        return self.uiDraw.tablOptDraw.currentIndex().row()

    def getRowValues(self):
        """
        @name: getRowValues
        @param: No recibe parametros
        @description: Obtiene la data que tiene cada fila y los agrega a una lista.
        @return: Retorna una lista de lista con los items de la tabla.
        """
        indexRow = self.getIndexRow()
        listItems = []
        for i in range(5):
            item = self.uiDraw.tablOptDraw.model().index(indexRow, i)
            value = self.uiDraw.tablOptDraw.model().data(item)
            listItems.append(value)
        return  listItems