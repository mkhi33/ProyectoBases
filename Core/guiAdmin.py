#-*-coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowAdmi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget



class GUIAdmin(QMainWindow):
    def __init__(self, parent = None):

        super(GUIAdmin, self).__init__(parent)
        self.uiAdmin = Ui_MainWindow()
        self.uiAdmin.setupUi(self)
        self.uiAdmin.btnCancel.setVisible(False)
        self.uiAdmin.btnSaveUser.setVisible(False)
        self.position = (0,0)




    def setHorizontalHeaderItem(self, size):
        for i in range(size):
            self.position = self.uiAdmin.tableWidget.rowCount()
            self.uiAdmin.tableWidget.insertRow(self.position)
            self.uiAdmin.tableWidget.resizeRowsToContents()

    def deleteAllRows(self):
        # Obtener el modelo de la tabla
        model:QAbstractTableModel = self.uiAdmin.tableWidget.model()
        # Remover todos las filas
        model.removeRows(0, model.rowCount())
        return True

    def updateTable(self, content = []):
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

        return self.uiAdmin.tableWidget.currentIndex().row()

    def getRowValues(self):
        indexRow = self.getIndexRow()
        listItems = []
        for i in range(9):
            item = self.uiAdmin.tableWidget.model().index(indexRow, i)
            value = self.uiAdmin.tableWidget.model().data(item)
            listItems.append(value)
        return  listItems



