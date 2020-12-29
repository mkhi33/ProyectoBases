#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import mysql.connector
from Core.ConnectionConfig import *


class MySqlEngine:
    """
    Esta clase gestiona el acceso a la base de datos.
    """
    def __init__(self, config):
        """
        @name __init__: Constructor de la clase MySqlEngine
        @param config: Objeto de configuración encapsulado con los parametros de acceso a la base de datos.
        @description: Gestiona el CRUD de la base de datos.
                        server: Servidor donde se encuentra la base de datos.
                        port: puerto
                        user: Usuario de la base de datos
                        password: contraseña de acceso a la base de datos SQL
                        database: Nombre de la base de datos.

        """

        self.server = config.server
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database
        self.start()   

    def start(self):
        """
        @name: start
        @param: No recibe parametros.
        @description: Inicia la base de datos con los parametros de conexión, Instanciando un cursor
        return: No retorna
        """

        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.link = self.con.cursor()

    def close(self):
        """
        @name: close
        @param: no recibe parametros
        @description: cierra la base de datos
        @return: No retorna.
        """
        self.con.close()
        return  True

    def select(self ,query = ""):
        """
        @name: select
        @param query: consulta hacia la base de datos.
        @description: Realiza una consulta de tipo SELECT a la base de datos.
        @return: Retorna una lista con las tuplas obtenidas mediante esta consulta.
        """
        self.link.execute(query)

        return self.link.fetchall()

    def insert(self,query):
        """
        @name: insert
        @param query: consulta hacia la base de datos.
        @description: Realiza una consulta de tipo INSERT a la base de datos.
        @return: True
        """
        self.link.execute(query)
        self.con.commit()
        return True

    def delete(self, query):
        """
        @name: delete
        @param query: consulta hacia la base de datos.
        @description: Realiza una consulta de tipo DELETE a la base de datos.
        @return: True
        """
        self.link.execute(query)
        self.con.commit()
        return True
        
    
    def update(self,query):
        """
        @name: update
        @param query: consulta hacia la base de datos.
        @description: Realiza una consulta de tipo UPDATE a la base de datos.
        @return: True
        """
        self.link.execute(query)
        self.con.commit()
        return True
        
        

