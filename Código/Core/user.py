"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
class User:
    """
    Esta clase encapsula los atributos de usuario.
    """

    def __init__(self, name, lastName, email, password, userName, gender, userType, birthDate):
        """
        @name: __init__
        @param name: Nombre del usuario ->String
        @param lastName: Apellido del usuario ->String
        @param email: Correo del usuario ->String
        @param password: Contraseña del usuario ->String
        @param  userName: Nombre del usuario -> String
        @param  gender: Genero del usuario ->String
        @param  userType: Tipo de uauario ->String
        @param birthDate: Fecha de nacimiento del usuario
        """
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.userName = userName
        self.gender = gender
        self.userType = userType
        self.birthDate = birthDate
    