import mysql.connector
from Core.ConnectionConfig import *


class MySqlEngine:
    def __init__(self, config):

        self.server = config.server
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database
        self.start()   

    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.link = self.con.cursor()

    def close(self):
        self.con.close()
        return  True

    def select(self ,query = ""):
        self.link.execute(query)

        return self.link.fetchall()

    def insert(self,query):
        self.link.execute(query)
        self.con.commit()
        return True

    def delete(self, query):
        self.link.execute(query)
        self.con.commit()
        return True
        
    
    def update(self,query):
        self.link.execute(query)
        self.con.commit()
        return True
        
        

