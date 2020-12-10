#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""

import json
from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
import configparser
class DBManager:
    """
    @name: DBManager
    @description: Esta clase se encarga de gestionar las consultas realizadas por el usuario hacia la base de datos.
    """
    def __init__(self):
        """
        @name __init__
        @param: No recibe parametros.
        @description: Constructor de la clase DBManager.
        @Attribute configA: Nombre de la sesión de el archivo config.ini que contiene la configuración de la base de datos A.
        @Attribute configB: Nombre de la sesión de el archivo config.ini que contiene la configuración de la base de datos B.
        @Attributte engine: Gestor de la base de datos A.
        @Attributte engineB: Gestor de la base de datos B.
        """
        self.configA = ConnectionConfig("ConfigurationA")
        self.configB = ConnectionConfig("ConfigurationB")
        self.engine = MySqlEngine(self.configA)
        self.engineB = MySqlEngine(self.configB)

    def getIni(self):
        """
        @name getIni
        @param: No recibe parametros.ArithmeticError
        @description: Mediante el uso de la libreria configparser se obtiene la configuración del archivo config.ini
        @return No retorna.
        """
        configuration = configparser.ConfigParser()
        configuration.write()
        config = configuration.read('config.ini')


    def login(self, name, password, userType):
        """
        @name login
        @param name: Nombre de usuario a autenticar.
        @param password: Contraseña del usuario a autenticar.
        @param userType: Tipo de usuario a autenticar (Administrador/ Operador)
        @description: Realiza la consulta a la base de datos para verificar si el usuario cumple con los requisitos para autenticar. 
        @return: Booleano
        """
        self.engine.start()
        query = """
        SELECT fk_var_user_name, txt_password FROM User
            WHERE fk_var_user_name = '%s' AND txt_password = AES_ENCRYPT('%s','%s') AND enu_type = '%s'
        """%(name, password,password,userType )
  
        if(len(self.engine.select(query))>0):
            return True
        self.engine.close()
        return False



    def registry(self,objUser):
        """
        @name: registry
        @param objUser: Objeto encapsulado 'usuario'
        @description: Segun los atributos encapsulados dentro de el objeto usuario se hace una consulta a la base de datos para insertar el elemento dentro de la tabla de usuarios.
        """
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
                    ('%s',AES_ENCRYPT('%s', '%s'), '%s', '%s', '%s', '%s')
                """%(userName,password, password,email,gender, userType, birthDate)
            self.engine.insert(insertUser)
        except AssertionError as error:
            self.engine.close()
    
    def getUsers(self):
        """
        @name getUsers
        @param: No recibe parametros
        @description: Hace una consulta a la base de datos para obtener todos los usuarios registrados.
        @return: Retorna una lista de tuplas con el resultado de la consulta.
        """
        self.engine.start()
        query = """
        SELECT id, fk_var_user_name,txt_name, txt_last_name, var_email,dat_birthdate, enu_gender, enu_type,txt_password  
            FROM (User JOIN FullName ON fk_var_user_name = FullName.var_user_name);
        """
        query = self.engine.select(query)
        self.engine.close()
        return query



    def updateUser(self, objUser, primariKey):
        """
        @name updateUser
        @param objUser: Objeto encapsulado Usuario
        @primariKey: Clave primaria del usuario a actualizar.
        @description: Actualiza un elemento dentro de la tabla User de la base de datos.
        @return: No retorna.

        """
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
                    UPDATE User SET  txt_password = AES_ENCRYPT('%s','%s'), var_email = '%s', enu_gender = '%s', enu_type = '%s', dat_birthdate = '%s'
                    WHERE fk_var_user_name = '%s';
                """%(password, password,email,gender, userType, birthDate, userName)
            
            self.engine.update(updateUser)  
        except:
            pass
        self.engine.close()

    def delete(self,userName):
        """
        @name: delete
        @param userName: Nombre de usuario a eliminar dentro de la base de datos.
        @description: Elimina un usuario dentro de la base de datos segun el user name.
        @return: No retorna

        """
        self.engine.start()
        try:
            deleteUser = "DELETE FROM User WHERE fk_var_user_name = '%s' "%(userName)
            self.engine.delete(deleteUser)
            deleteFullName = "DELETE FROM FullName WHERE var_user_name = '%s'"%(userName)

            self.engine.delete(deleteFullName)
        except:
            pass
        self.engine.close

    def saveDraw(self, name, jsonFile, idUser):
        """
        @name: saveDraw
        @param jsonFile: Contenido de archivo JSON con la configuración del dibujo.
        @param idUser: id del usuario que creo el dibujo. 
        @description: Guarda un dibujo en la base de datos según el usuario que lo haya creado.
        @return: No retorna.
        """
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
        """
        @name: editDraw
        @param name: Nobre del dibujo a editar.
        @param jsonFile: JSON con la configuración del dibujo.
        @paramidUSer: Id del usuario propietario del dibujo.
        @param idDraw: Id del dibujo que se va a modificar.
        """
        self.engine.start()
        self.engineB.start()
        updateA = """
                UPDATE Drawing SET txt_name = '%s', jso_file = '%s' WHERE fk_id_usuario = %s AND id = %s
                """ % (name, jsonFile, idUser, idDraw)

        updateB = """
        UPDATE DrawingB SET blo_jso_file = compress('%s') WHERE int_id_user = %s AND id = %s
        """ % (jsonFile, idUser, idDraw)
        self.engine.update(updateA)
        self.engineB.update(updateB)
        self.engine.close()
        self.engineB.close()

    def getDraw(self, idDraw):
        """
        @name: getDraw
        @param idDraw: Id del dibujo a obtener.
        @description: Obtiene un dibujo dentro de la base de datos según el id.
        @return Retorna una lista con el resultado de la consulta realizada.
        """
        self.engine.start()
        query = """
        SELECT jso_file FROM Drawing WHERE id = %s
        """ % (idDraw)
        query = self.engine.select(query)
        self.engine.close()
        return query

    def getAllDraws(self):
        """
        @name: getAllDraws
        @param: No recibe parametros.
        @description: Obtiene el informe de todos los dibujos de la base de datos a excepción de la configuración del archivo JSON.
        @return: Retorna una lista con el resultado de la consulta.
        """
        self.engine.start()
        query = """
                SELECT id, fk_id_Usuario, txt_name, dat_creation_date, tim_modification_date FROM Drawing;
            """
        draws = self.engine.select(query)
        self.engine.close()
        return draws

    def getDrawing(self, fkIdUser):
        """
        @name:getDrawing
        @param fkIdUser: id del usuario al que pertenecen los dibujos.
        @description: Obtiene todos los dibujos de la base de datos de un determinado usuario según el id de usuario.
        @return: Retorna una lista con el resultado de la consulta.
        """

        self.engine.start()
        query = """
            SELECT id, fk_id_Usuario, txt_name, dat_creation_date, tim_modification_date FROM Drawing WHERE fk_id_Usuario = %s;
        """ % fkIdUser
        query = self.engine.select(query)
        self.engine.close()
        return query

    def getDrawingB(self, idDraw):
        """
        @name getDrawingB
        @param idDraw: Id del dibujo a obtener desde la base de datos B.
        @description: Obtiene un dibujo de la base de datos B según el id de dibujo.
        @return Retorna una lista con el resultado de la consulta.
        """
        self.engineB.start()
        query = """
            SELECT  uncompress(blo_jso_file) FROM DrawingB WHERE id = %s;
        """%idDraw
        query = self.engineB.select(query)
        self.engineB.close()
        return query

    def deleteDraw(self, id):
        """
        @name: deleteDraw
        @param id: Id del dibujo a eliminar
        @description: Elimina un dibujo de la base de datos según su id.
        @return No retorna
        """
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
        """
        @name: setFillColor
        @param fillColor: configuración de color fillcolor
        @description: Asigna una configuración de color fillcolor al editor de dibujo.
        @return: no retorna
        """
        self.engine.start()
        update = """
                 UPDATE Color SET var_fill_color = '%s'
                 """ % (fillColor )
        self.engine.update(update)

    def setPenColor(self, penColor):
        """
        @name: setPenColor
        @param pencolor: configuración de color pencolor
        @description: Asigna una configuración de color pencolor al editor de dibujo.
        @return: no retorna
        """
        self.engine.start()
        update = """
                 UPDATE Color SET var_pen_color = '%s'
                 """ % (penColor )
        self.engine.update(update)


    def getFillColor(self):
        """
        @name: getFillColor
        @param: No recibe parametros.
        @description Obtiene el color de configuración fillcolor dentro de la base de datos dentro de la tabla Color.
        @return No retorna.
        """
        self.engine.start()
        query = """
        SELECT var_fill_color FROM Color LIMIT 1;
        """
        query = self.engine.select(query)
        self.engine.close()
        return query

    def getPenColor(self):
        """
        @name: getPenColor
        @param: No recibe parametros.
        @description Obtiene el color de configuración penColor de la base de datos dentro de la tabla Color.
        @return No retorna.
        """
        query = """
        SELECT var_pen_color FROM Color LIMIT 1;
        """
        query = self.engine.select(query)
        self.engine.close()
        return query

    def setLoginRegister(self, idUser, fillColor, penColor):
        """
        @name: setLoginRegister
        @param idUser: Id del usuario que se esta autenticando.
        @param fillColor: Configuración actual de color.
        @param penColor: Configuración actual de color.
        @description: Agrega un registro de Autenticación a la tabla de registro.
        @return: No retorna.
        """
        self.engine.start()
        query = """
        INSERT INTO Registry  (enu_action, fk_id_usuario, var_fill_color, var_pen_color) VALUES
            ('Autenticación', %s ,'%s', '%s' )
            
        """%(int(idUser),fillColor, penColor )
        self.engine.insert(query)
        self.engine.close()
    def setVisualitation(self, idDraw, idUser, fillColor, penColor):
        """
        @name setVisualitation
        @param idDraw: Id del dibujo que se visualiza.
        @param idUser: Id del usuario que visualiza el dibujo.
        @param fillColor: Configuración de color fillcolor
        @param penColor: Configuración de color pencolor
        @description: Registra una visualización de dibujos dentro de la tabla de registros.
        @return No retorna.
        """
        self.engine.start()
        query = """
        INSERT INTO Registry (enu_action, fk_id_usuario, fk_id_dibujo, var_fill_color, var_pen_color) VALUES
            ('Visualización', %s, %s,'%s', '%s' )
            

        """ % (idUser, idDraw, fillColor, penColor)

        self.engine.insert(query)
        self.engine.close()
    def setConfigurationPenColor(self, idUser, pencolor, fillcolor):
        """
        @name: setConfigurationPenColor
        @param idUser: Id de usuario que configura el color
        @param  penColor: Color para pencolor
        @param  fillColor: Color de fillcolor.
        @description:  Registra una nueva configuración para pencolor y fillcolor dentro de la tabla Registry.
        return No retorna
        """
        self.engine.start()
        query = """
        INSERT INTO Registry (enu_action, fk_id_usuario, var_fill_color, var_pen_color) VALUES
            ('Configuración', %s, '%s', '%s')
        """%(idUser, fillcolor, pencolor)

        self.engine.insert(query)
        self.engine.close()
    def getRegistries(self, idUser):
        """
        @name: getRegistries
        @param idUser Id usuario que se obtendran los registros de l atabla Registry.
        @description: Obtiene un informe de las acciones que ha realizado el usuario.
        æreturn Retorna una lista según la consulta realizada.
        """
        self.engine.start()
        query = """
        SELECT *  FROM Registry WHERE fk_id_usuario = %s
        """%idUser
        query = self.engine.select(query)
        self.engine.close()
        return query
