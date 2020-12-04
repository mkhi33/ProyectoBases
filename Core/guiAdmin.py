#-*-coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Core.pyQt5.windowAdmi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget



class GUIAdmin(QMainWindow):
    def __init__(self, parent = None):

        super(GUIAdmin, self).__init__(parent)
        self.uiAdmin = Ui_MainWindow()
        self.uiAdmin.setupUi(self)
        

        


    def updateTable(self, content = []):
        
        for i in range(len(content)):
            id = "%s"%content[i][0]
            name = "%s"%content[i][1]
            lastName = "%s"%content[i][2]
            email = "%s"%content[i][3]
            birthDate = "%s"%content[i][4]
            gender = "%s"%content[i][5]
            typeUser = "%s"%content[i][6]

            itemId = QTableWidgetItem(id)
            itemName = QTableWidgetItem(name)
            itemLastName = QTableWidgetItem(lastName)
            itemEmail = QTableWidgetItem(email)
            itemBirthDate = QTableWidgetItem(birthDate)
            itemGender = QTableWidgetItem(gender)
            itemTypeUser = QTableWidgetItem(typeUser)

            itemId.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemName.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemLastName.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemEmail.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemBirthDate.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemGender.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            itemTypeUser.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )


            self.uiAdmin.tableWidget.setItem(i,0, itemId)
            self.uiAdmin.tableWidget.setItem(i,1,itemName )
            self.uiAdmin.tableWidget.setItem(i,2,itemLastName )
            self.uiAdmin.tableWidget.setItem(i,3, itemEmail )
            self.uiAdmin.tableWidget.setItem(i,4,itemBirthDate )
            self.uiAdmin.tableWidget.setItem(i,5,itemGender )
            self.uiAdmin.tableWidget.setItem(i,6, itemTypeUser)



            