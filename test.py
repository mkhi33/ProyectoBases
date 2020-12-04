from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine

"""
En este script se hacen las pruebas para el proyecto:

    la clase MySqlEngine tiene la referencia a la base de datos.
"""

config = ConnectionConfig("localhost","3306", "admin", "admin", "DataBaseA")

engine = MySqlEngine(config)
user = engine.select("SELECT * FROM User")

def registryFullName(userName, name, lastName):
 
    query = """INSERT INTO FullName (var_user_name, txt_name, txt_last_name) 
                           VALUES 
                           ('%s', '%s', '%s') """%(userName, name, lastName)
    engine.insert(query)
    
def updateUser(obj):
    pass

def delete(id):
    # Tambien puede recibir como parametro el nombre de usuario
    pass
#registryFullName("@user01", "Nombre", "Apellido")


