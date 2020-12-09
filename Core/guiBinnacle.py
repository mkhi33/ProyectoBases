#-*-coding:utf-8 -*-
import sys
from datetime import date

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from Core.pyQt5.windowBinnacle import Ui_MainWindow


class GuiBinnacle(QMainWindow):
    def __init__(self, parent = None):

        super(GuiBinnacle, self).__init__(parent)
        self.uiBinnacle = Ui_MainWindow()
        self.uiBinnacle.setupUi(self)

    def deleteAllRows(self):
        # Obtener el modelo de la tabla
        model:QAbstractTableModel = self.uiBinnacle.tblBitacora.model()
        # Remover todos las filas
        model.removeRows(0, model.rowCount())
        return True

    def setHorizontalHeaderItem(self, size):
        for i in range(size):
            self.position = self.uiBinnacle.tblBitacora.rowCount()
            self.uiBinnacle.tblBitacora.insertRow(self.position)
            self.uiBinnacle.tblBitacora.resizeRowsToContents()

    def updateTable(self, content = []):
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
        return self.uiBinnacle.tblBitacora.currentIndex().row()

    def getRowValues(self):
        indexRow = self.getIndexRow()
        listItems = []
        for i in range(5):
            item = self.uiBinnacle.tblBitacora.model().index(indexRow, i)
            value = self.uiBinnacle.tblBitacora.model().data(item)
            listItems.append(value)
        return  listItems

