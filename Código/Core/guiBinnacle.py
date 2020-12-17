#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import sys
from datetime import date

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from Core.pyQt5.windowBinnacle import Ui_MainWindow


class GuiBinnacle(QMainWindow):
    """
    @name: GuiBinnacle
    @Description: Esta clase hereda de QMainWindow y gestiona una instancia de la ventana De bitacora de usuarios.
    """
    def __init__(self, parent = None):
    

        super(GuiBinnacle, self).__init__(parent)
        self.uiBinnacle = Ui_MainWindow()
        self.uiBinnacle.setupUi(self)
        self.centerWindow()

    def deleteAllRows(self):
        """
        @name: deleteAllRows
        @param: No recibe parametros
        @description: Elimina todas las filas de una QTableWidget
        @return: True.
        """
        model:QAbstractTableModel = self.uiBinnacle.tblBitacora.model()
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
            self.position = self.uiBinnacle.tblBitacora.rowCount()
            self.uiBinnacle.tblBitacora.insertRow(self.position)
            self.uiBinnacle.tblBitacora.resizeRowsToContents()

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
            date = str(content[i][1])
            action = str(content[i][2])
            idUser = str(content[i][3])
            idDraw = str(content[i][4])
            fillColor = str(content[i][5])
            penColor = str(content[i][5])

            if idDraw == "None":
                idDraw = "-"

            itemId = QTableWidgetItem(id)
            itemDate = QTableWidgetItem(date)
            itemAction = QTableWidgetItem(action)
            itemIdUser = QTableWidgetItem(idUser)
            itemIdDraw = QTableWidgetItem(idDraw)
            itemFillColor = QTableWidgetItem(fillColor)
            itemPenColor = QTableWidgetItem(penColor)

            itemId.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemDate.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemAction.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemIdUser.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemIdDraw.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemFillColor.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            itemPenColor.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.uiBinnacle.tblBitacora.setItem(i, 0, itemAction)
            self.uiBinnacle.tblBitacora.setItem(i, 1, itemDate)
            self.uiBinnacle.tblBitacora.setItem(i, 2, itemIdUser)
            self.uiBinnacle.tblBitacora.setItem(i, 3, itemIdDraw)
            self.uiBinnacle.tblBitacora.setItem(i, 4, itemPenColor)
            self.uiBinnacle.tblBitacora.setItem(i, 5, itemFillColor)
            #self.uiBinnacle.tblBitacora.setItem(i, 6, itemPenColor)

    def getIndexRow(self):
        """
        @name: getIndexRow
        @param: No recibe parametros.
        @description: Obtiene el indice de la fila seleccionada por el usuario.
        @return retorna la fila seleccionada. 
        """
        return self.uiBinnacle.tblBitacora.currentIndex().row()

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
            item = self.uiBinnacle.tblBitacora.model().index(indexRow, i)
            value = self.uiBinnacle.tblBitacora.model().data(item)
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