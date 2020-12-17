DROP DATABASE IF EXISTS DataBaseB ;
CREATE DATABASE DataBaseB CHARACTER SET utf8;

USE DataBaseB;

CREATE TABLE DrawingB(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "id autoincrementable, llave primaria",
    blo_jso_file BLOB NOT NULL COMMENT "Json en formato BLOB",
    int_id_user INT NOT NULL COMMENT "Id del usuarop propietario del dibujo."
) COMMENT "En esta tabla se almacenan una copia del dibujo que se guarda en la base de datos A.";
