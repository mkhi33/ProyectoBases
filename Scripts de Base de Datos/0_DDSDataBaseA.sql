DROP DATABASE IF EXISTS DataBaseA ;
CREATE DATABASE DataBaseA CHARACTER SET utf8;

USE DataBaseA;

CREATE TABLE FullName(
    
    var_user_name VARCHAR(10)  PRIMARY KEY COMMENT "Nombre de usuario",
    txt_name TEXT NOT NULL COMMENT "Nombre real del usuario",
    txt_last_name TEXT NOT NULL COMMENT "Apellido real del usuario"
) COMMENT "En esta tabla se guarda el nombre completo de un usuario.";

CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "id autoincrementable, llave primaria" ,
    fk_var_user_name VARCHAR(15) NOT NULL COMMENT "Llave forranea, nombre del usuario de la tabla FullName",
    txt_password BLOB NOT NULL COMMENT "Contraseña del usuario cifrada con AES_ENCRYPT",
    var_email VARCHAR(50) NOT NULL COMMENT "Correo electronico del usuario.",
    enu_gender ENUM('M', 'F') COMMENT "Genero del usuario M: Masculino, F: Femenino",
    enu_type ENUM('Administrador', 'Operador') COMMENT "Tipo de usuario, Administrador/Operador" ,
    dat_birthdate DATETIME NOT NULL COMMENT "Fecha de nacimiento del usuario",
    
    FOREIGN KEY (fk_var_user_name)
        REFERENCES FullName(var_user_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT uniq_user UNIQUE (fk_var_user_name , var_email) COMMENT "Integridad referencial hacia la tabla FullName"

) COMMENT "Tabla que guarda los usuarios registrados en la base de datos.";

CREATE TABLE Drawing(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT  "ID autoincrementable, llave primaria",
    txt_name TEXT NOT NULL COMMENT "Nombre del dibujo que se guardara en esta tabla." ,
    dat_creation_date DATETIME DEFAULT NOW() COMMENT "Fecha de creación",
    tim_modification_date TIMESTAMP DEFAULT NOW() ON UPDATE NOW() COMMENT "Tiempo de modificación.",
    jso_file JSON NOT NULL COMMENT "Tipo de dato JSON que almacena la configuración del dibujo.",
    fk_id_usuario INT NOT NULL COMMENT "Llave foranea del usuario propietario de este dibujo.",

    FOREIGN KEY (fk_id_usuario)
        REFERENCES User(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) COMMENT "Tabla que guarda los datos de registro de un dibujo.";

CREATE TABLE Registry(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Id autoincrementable, llave primaria",
    tim_date TIMESTAMP DEFAULT NOW() COMMENT "Fecha del registro, por defecto es la fecha actual.",
    enu_action ENUM('Autenticación', 'Visualización', 'Creación', 'Modificación','Eliminación', 'Configuración', '-') DEFAULT '-' COMMENT "Enum de las acciones que puede ejecutar el usuario." ,
    fk_id_usuario INT NOT NULL COMMENT "Llave foranea del usuario propietario de el registro.",
    fk_id_dibujo INT DEFAULT NULL COMMENT "Llave foranea del dibujo, puede ser Null" ,
    var_fill_color VARCHAR(15) NOT NULL COMMENT "Varchar que contiene el color de configuaración fillcolor " ,
    var_pen_color VARCHAR(15) NOT NULL COMMENT "Varchar que contiene el color de configuaración pencolor",
    FOREIGN KEY (fk_id_usuario)
        REFERENCES User(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) COMMENT "Tabla que guarda los registros de la actividad que ha tenido el usuario dentro del programa.";

CREATE TABLE Color(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Id autoincrementable, llave primaria",
    var_fill_color VARCHAR(15) NOT NULL COMMENT "varchar con el código de color",
    var_pen_color VARCHAR(15) NOT NULL COMMENT "Varchar con el código de color"
) COMMENT "Almacena la configuración de colores pencolor y fillcolor realizada por el usuario administrador.";
