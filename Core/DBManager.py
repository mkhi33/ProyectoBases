from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
class DBManager:
    def __init__(self):
        self.config = ConnectionConfig("localhost","3306", "admin", "admin", "DataBaseA")
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
        query =  "SELECT * FROM User;"
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
            self.engine.delete(deleteFullName)
            print("Se elimino")
        except:
            print("No se pudo eliminar")

        


        
