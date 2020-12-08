from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
from Core.DBManager import DBManager
from Core.user import User
from Core.encrypt import *
from Core.compress import Compress



DBM = DBManager()
e = Encriptacion()

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
    file = open("JsonSinEncriptar.json", "w")
    file.write(draw[0][0])
    file.close()
    return draw[0][0]

def encriptJSON():
    draw = getDraw()
    jsonEncrypt = e.encriptar((draw))
    file = open("Jsoncriptado.txt", "w")
    file.write(jsonEncrypt)
    file.close()
    return True
def decrypt():
    file = open("Jsoncriptado.txt", 'r')
    content = file.read()
    file.close()
    d = Desencriptacion()
    jsonDecrypt = d.Desencriptar(content)
    fileDecrypt = open('JsonDecpt.json', "w")

    fileDecrypt.write(jsonDecrypt)
    fileDecrypt.close()

def compress():
    file = open("JsonSinEncriptar.json", "r")
    jsonData = file.read()
    c = Compress()
    c.compress(jsonData)
    file.close()

import configparser

def configParser():
    config = configparser.RawConfigParser()

    # Please note that using RawConfigParser's set functions, you can assign
    # non-string values to keys internally, but will receive an error when
    # attempting to write to a file or when you get it in non-raw mode. Setting
    # values using the mapping protocol or ConfigParser's set() does not allow
    # such assignments to take place.
    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    # Writing our configuration file to 'example.cfg'
    with open('example.cfg', 'w') as configfile:
        config.write(configfile)

def getIni():
    config = configparser.ConfigParser()
    config.read('example.cfg')
    print(config.get('Section1', 'foo'))

def getDraw():
    draw = DBM.getDrawingB(2)[0][0]
    print(draw)
getDraw()



