from builtins import print
import json
from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
import configparser
class DBManager:
    def __init__(self):
        self.configA = ConnectionConfig("ConfigurationA")
        self.configB = ConnectionConfig("ConfigurationB")
        #self.config = ConnectionConfig(self.host,self.port, self.user,self.password, self.database)
        self.engine = MySqlEngine(self.configA)
        self.engineB = MySqlEngine(self.configB)

    def getIni(self):
        configuration = configparser.ConfigParser()
        configuration.write()
        config = configuration.read('config.ini')


    def login(self, name, password, userType):
        self.engine.start()
        query = """
        SELECT fk_var_user_name, txt_password FROM User
            WHERE fk_var_user_name = '%s' AND txt_password = '%s' AND enu_type = '%s'
        """%(name, password,userType )
  
        if(len(self.engine.select(query))>0):
            return True
        self.engine.close()
        return False



    def registry(self,objUser):
        self.engine.start()
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
        except AssertionError as error:
            print(error)
            print("No se agrego")
            self.engine.close()
    
    def getUsers(self):
        self.engine.start()
        query = """
        SELECT id, fk_var_user_name,txt_name, txt_last_name, var_email,dat_birthdate, enu_gender, enu_type,txt_password  
            FROM (User JOIN FullName ON fk_var_user_name = FullName.var_user_name);
        """
        query = self.engine.select(query)
        self.engine.close()
        return query



    def updateUser(self, objUser, primariKey):
        self.engine.start()
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
        self.engine.close()

    def delete(self,userName):
        self.engine.start()
        try:
            # Tambien puede recibir como parametro el nombre de usuario
            deleteUser = "DELETE FROM User WHERE fk_var_user_name = '%s' "%(userName)
            self.engine.delete(deleteUser)
            deleteFullName = "DELETE FROM FullName WHERE var_user_name = '%s'"%(userName)

            self.engine.delete(deleteFullName)
            print("Se elimino")
        except:
            print("No se pudo eliminar")
        self.engine.close

    def saveDraw(self, name, jsonFile, idUser):
        self.engine.start()
        self.engineB.start()
        insertDrawA = """
                INSERT INTO Drawing(txt_name, jso_file, fk_id_usuario) VALUES
                ('%s','%s', %s)"""%(name, jsonFile, idUser)

        insertDrawB = """
        INSERT INTO DrawingB(blo_jso_file, int_id_user) VALUES
        (compress('%s'),%s)
        """%(jsonFile, idUser)

        self.engine.insert(insertDrawA)
        self.engineB.insert(insertDrawB)

        self.engine.close()
        self.engineB.close()

    def editDraw(self, name, jsonFile, idUser, idDraw):
        self.engine.start()
        self.engineB.start()
        updateA = """
                UPDATE Drawing SET txt_name = '%s', jso_file = '%s' WHERE fk_id_usuario = %s AND id = %s
                """%(name, jsonFile, idUser, idDraw)

        updateB = """
        UPDATE DrawingB SET blo_jso_file = compress('%s') WHERE int_id_user = %s AND id = %s
        """%(jsonFile, idUser, idDraw)
        self.engine.update(updateA)
        self.engineB.update(updateB)
        self.engine.close()
        self.engineB.close()

    def getDraw(self, idDraw):
        self.engine.start()
        query = """
        SELECT jso_file FROM Drawing WHERE id = %s
        """%(idDraw)
        query = self.engine.select(query)
        self.engine.close()
        return query

    def getAllDraws(self):
        self.engine.start()
        query = """
                SELECT id, fk_id_Usuario, txt_name, dat_creation_date, tim_modification_date FROM Drawing;
            """
        draws = self.engine.select(query)
        self.engine.close()
        return draws

    def getDrawing(self, fkIdUser):
        self.engine.start()
        query = """
            SELECT id, fk_id_Usuario, txt_name, dat_creation_date, tim_modification_date FROM Drawing WHERE fk_id_Usuario = %s;
        """%fkIdUser
        query = self.engine.select(query)
        self.engine.close()
        return query
    def getDrawingB(self, idDraw):
        self.engineB.start()
        query = """
            SELECT  uncompress(blo_jso_file) FROM DrawingB WHERE id = %s;
        """%idDraw
        query = self.engineB.select(query)
        self.engineB.close()
        return query
    def deleteDraw(self, id):
        self.engine.start()
        self.engineB.start()
        queryA = """
        DELETE FROM Drawing WHERE id = %s
        """%id
        self.engine.delete(queryA)

        queryB = """
        DELETE From DrawingB WHERE id = %s
        """%id
        self.engineB.delete(queryB)
        self.engine.close()
        self.engineB.close()

        return True
    def setFillColor(self, fillColor):
        self.engine.start()
        update = """
                 UPDATE Color SET var_fill_color = '%s'
                 """ % (fillColor )
        self.engine.update(update)

    def setPenColor(self, penColor):
        self.engine.start()
        update = """
                 UPDATE Color SET var_pen_color = '%s'
                 """ % (penColor )
        self.engine.update(update)


    def getFillColor(self):
        self.engine.start()
        query = """
        SELECT var_fill_color FROM Color LIMIT 1;
        """
        query = self.engine.select(query)
        self.engine.close()
        return query

    def getPenColor(self):
        query = """
        SELECT var_pen_color FROM Color LIMIT 1;
        """
        query = self.engine.select(query)
        self.engine.close()
        return query

    def setLoginRegister(self, idUser, fillColor, penColor):
        self.engine.start()
        query = """
        INSERT INTO Registry  (enu_action, fk_id_usuario, var_fill_color, var_pen_color) VALUES
            ('Autenticación', %s ,'%s', '%s' )
            
        """%(int(idUser),fillColor, penColor )
        print(query)
        self.engine.insert(query)
        self.engine.close()
    def setVisualitation(self, idDraw, idUser, fillColor, penColor):
        self.engine.start()
        query = """
        INSERT INTO Registry (enu_action, fk_id_usuario, fk_id_dibujo, var_fill_color, var_pen_color) VALUES
            ('Visualización', %s, %s,'%s', '%s' )
            

        """ % (idUser, idDraw, fillColor, penColor)

        self.engine.insert(query)
        self.engine.close()
    def setConfigurationPenColor(self, idUser, pencolor, fillcolor):
        self.engine.start()
        query = """
        INSERT INTO Registry (enu_action, fk_id_usuario, var_fill_color, var_pen_color) VALUES
            ('Configuración', %s, '%s', '%s')
        """%(idUser, fillcolor, pencolor)

        self.engine.insert(query)
        self.engine.close()
    def getRegistries(self, idUser):
        self.engine.start()
        query = """
        SELECT * FROM Registry WHERE fk_id_usuario = %s
        """%idUser
        print(idUser)
        print(query)
        query = self.engine.select(query)
        self.engine.close()
        return query
