#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from Core.pyQt5.windowDraw import Ui_MainWindow
from PyQt5.QtCore import Qt, QAbstractTableModel


class GuiDraw(QMainWindow):
    def __init__(self, parent = None):

        super(GuiDraw, self).__init__(parent)
        self.uiDraw = Ui_MainWindow()
        self.uiDraw.setupUi(self)
    def deleteAllRows(self):
        # Obtener el modelo de la tabla
        model:QAbstractTableModel = self.uiDraw.tablOptDraw.model()
        # Remover todos las filas
        model.removeRows(0, model.rowCount())
        return True
    def setHorizontalHeaderItem(self, size):
        for i in range(size):
            self.position = self.uiDraw.tablOptDraw.rowCount()
            self.uiDraw.tablOptDraw.insertRow(self.position)
            self.uiDraw.tablOptDraw.resizeRowsToContents()

    def updateTable(self, content = []):
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
        return self.uiDraw.tablOptDraw.currentIndex().row()

    def getRowValues(self):
        indexRow = self.getIndexRow()
        listItems = []
        for i in range(5):
            item = self.uiDraw.tablOptDraw.model().index(indexRow, i)
            value = self.uiDraw.tablOptDraw.model().data(item)
            listItems.append(value)
        return  listItems




