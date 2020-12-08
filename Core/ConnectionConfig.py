import configparser
class ConnectionConfig:

    def __init__(self, sesionConfig):
        self.server = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.database = ""
        #self.writeConfig()
        self.getConfig(sesionConfig)
    def writeConfig(self):
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
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def getConfig(self, configuration):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config.get(configuration, "host")
        self.port = config.get(configuration, "port")
        self.user = config.get(configuration, "user")
        self.password = config.get(configuration, "password")
        self.database = config.get(configuration, "database")



