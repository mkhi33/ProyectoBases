from builtins import print
import json
from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
import configparser
class DBManager:
    def __init__(self):
        self.configuration = configparser.ConfigParser()
        self.configuration['config'] = {'port': '3306', 'user': 'admin', 'password': 'admin', 'database': 'DataBaseA',
                            'host': 'localhost'}
        self.host = self.configuration['config']['host']
        self.user = self.configuration['config']['user']
        self.port = self.configuration['config']['port']
        self.password = self.configuration['config']['password']
        self.database = self.configuration['config']['database']


        self.config = ConnectionConfig(self.host,self.port, self.user,self.password, self.database)
        self.engine = MySqlEngine(self.config)

    def login(self, name, password, userType):
      
        query = """
        SELECT fk_var_user_name, txt_password FROM User
            WHERE fk_var_user_name = '%s' AND txt_password = '%s' AND enu_type = '%s'
        """%(name, password,userType )
  
        if(len(self.engine.select(query))>0):
            return True
        return False



    def registry(self,objUser):
        name = objUser.name
        lastName = objUser.lastName
        email = objUser.email
        password = objUser.password
        userName = objUser.userName
        gender = objUser.gender
        userType = objUser.userType
        birthDate = objUser.birthDate
        
        try:
            insertFullName = """INSERT INTO FullName (var_user_name, txt_name, txt_last_name) 
                                VALUES 
                                ('%s', '%s', '%s') """%(userName, name, lastName)
            self.engine.insert(insertFullName)  
            insertUser = """
                    INSERT INTO User(fk_var_user_name, txt_password, var_email, enu_gender, enu_type, dat_birthdate) VALUES
                    ('%s','%s', '%s', '%s', '%s', '%s');
                """%(userName,password,email,gender, userType, birthDate)
            self.engine.insert(insertUser)
            print("Si se agrego")
        except:
            print("No se agrego")
    
    def getUsers(self):
        query = """
        SELECT id, fk_var_user_name,txt_name, txt_last_name, var_email,dat_birthdate, enu_gender, enu_type,txt_password  
            FROM (User JOIN FullName ON fk_var_user_name = FullName.var_user_name);
        """
        return self.engine.select(query)



    def updateUser(self, objUser, primariKey):
        name = objUser.name
        lastName = objUser.lastName
        email = objUser.email
        password = objUser.password
        userName = objUser.userName
        gender = objUser.gender
        userType = objUser.userType
        birthDate = objUser.birthDate

        try:
            updateFullName = """UPDATE FullName SET var_user_name = '%s', txt_name = '%s', txt_last_name = '%s' 
                                WHERE var_user_name = '%s'
                            """%(userName, name, lastName, primariKey)
            self.engine.update(updateFullName)  
            updateUser = """
                    UPDATE User SET  txt_password = '%s', var_email = '%s', enu_gender = '%s', enu_type = '%s', dat_birthdate = '%s'
                    WHERE fk_var_user_name = '%s';
                """%(password,email,gender, userType, birthDate, userName)
            
            self.engine.update(updateUser)  
            print("Si se actualizo")
        except:
            print("No se actualizo")

    def delete(self,userName):
        try:
            # Tambien puede recibir como parametro el nombre de usuario
            deleteUser = "DELETE FROM User WHERE fk_var_user_name = '%s' "%(userName)
            self.engine.delete(deleteUser)
            deleteFullName = "DELETE FROM FullName WHERE var_user_name = '%s'"%(userName)
            print(userName)
            self.engine.delete(deleteFullName)
            print("Se elimino")
        except:
            print("No se pudo eliminar")

    def saveDraw(self, name, jsonFile, idUser):

        insertDraw = """
                INSERT INTO Drawing(txt_name, jso_file, fk_id_usuario) VALUES
                ('%s','%s', %s)"""%(name, jsonFile, idUser)
        self.engine.insert(insertDraw)

    def getDraw(self, idDraw):
        query = """
        SELECT jso_file FROM Drawing WHERE id = %s
        """%(idDraw)

        return self.engine.select(query)

    def getDrawing(self, fkIdUser):
        query = """
            SELECT id, fk_id_Usuario, txt_name, dat_creation_date, tim_modification_date FROM Drawing WHERE fk_id_Usuario = %s;
        """%fkIdUser
        return self.engine.select(query)