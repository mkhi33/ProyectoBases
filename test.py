from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
from Core.DBManager import DBManager
from Core.user import User

"""
En este script se hacen las pruebas para el proyecto:

    la clase MySqlEngine tiene la referencia a la base de datos.
"""

DBM = DBManager()

def testRegistry():
    name = "Anilcar Antonio"
    lastName = "Rodriguez Velasquez"
    email = "aarodriguezv@unah.hn"
    password = "pass"
    userName = "mkhi"
    gender = "M"
    userType = "Operador"
    birthDate = "1998-12-26"

    user = User(name , lastName, email, password, userName, gender, userType, birthDate)

    DBM.registry(user)

def testUpdateUser():
    name = "Anilcar Antonio"
    lastName = "Rodriguez Velasquez"
    email = "aarodriguezv@unah.hn"
    password = "contraseña"
    userName = "mkhi"
    gender = "M"
    userType = "Operador"
    birthDate = "1998-12-26"
    user = User(name , lastName, email, password, userName, gender, userType, birthDate)
    primaryKey = "mkhi"
    DBM.updateUser(user, primaryKey)

def testDelete():
    DBM.delete("mkhi")

def testUsers():
    user = DBM.getUsers()
    
    print(type(user))
    print(user)
    t = user[0]
def saveDraw():
    file = open('Dibujo.json','r')
    content = file.read()
    file.close()
    #content = content.replace("[", "{").replace("]", "}")

    DBM.saveDraw("Dibujo1","2020-12-04",content,9)
    print(content)

def getDraw():
    draw = DBM.getDraw(1)
    file = open("Query.json", "w")
    file.write(draw[0][0])
    file.close()
    print(draw)

#getDraw()
#saveDraw()
#testUsers()

#testUpdateUser()
#testDelete()


