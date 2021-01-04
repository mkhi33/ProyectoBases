"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
"""

import configparser
class ConnectionConfig:
    """
    @name ConectionConfig:
    @Description: Configura la base de datos para su uso segun la configuración establecida en el archivo config.ini
    """

    def __init__(self, sesionConfig):
        """

        @param sesionConfig: Es el nombre de la sesión en el archivo confif.ini (ConfigurationA/ ConfigurationB)
        """
        self.host = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.database = ""
        #self.writeConfig()
        self.getConfig(sesionConfig)
    def writeConfig(self):
        """
        @name: writeConfig
        @param: No recibe parametros.
        @description: Esta función genera un archivo config.ini con los parametros establecidos directamente en el código, este archivo se guarda dentro del directorio Core/config/config.ini y sirve para configurar el acceso a la base de datos.
        @return: No retorna
        """
        config = configparser.RawConfigParser()
        config.add_section("ConfigurationA")
        config.set("ConfigurationA", "host", "localhost")
        config.set("ConfigurationA", "port", "3306")
        config.set("ConfigurationA", "user", "admin")
        config.set("ConfigurationA", "password", "admin")
        config.set("ConfigurationA", "database", "DataBaseA")

        config.add_section("ConfigurationB")
        config.set("ConfigurationB", "host", "localhost")
        config.set("ConfigurationB", "port", "3306")
        config.set("ConfigurationB", "user", "admin")
        config.set("ConfigurationB", "password", "admin")
        config.set("ConfigurationB", "database", "DataBaseB")
        with open('Core/config/config.ini', 'w') as configfile:
            config.write(configfile)

    def getConfig(self, configuration):
        """
        @name: getConfig
        @param config: Sesión de configuración que se encuentra en el archivo config.ini.
        @description: Lee el archivo config.ini que contiene la configuración de acceso a la base de datos, obtiene sus atributos según la sesión que se recibe como parametro y se asigna a los atributos de la clase propia (self.host, self.port, ...)
        @return: No retorna.         
        """
        config = configparser.ConfigParser()
        config.read('Core/config/config.ini')
        self.host = config.get(configuration, "host")
        self.port = config.get(configuration, "port")
        self.user = config.get(configuration, "user")
        self.password = config.get(configuration, "password")
        self.database = config.get(configuration, "database")




