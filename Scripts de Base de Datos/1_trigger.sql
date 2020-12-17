DROP TRIGGER IF EXISTS tg_binnacle_create_draw;
DROP TRIGGER IF EXISTS tg_binnacle_update_draw;
DROP TRIGGER IF EXISTS tg_binnacle_delete_draw;

DELIMITER $$
CREATE TRIGGER tg_binnacle_create_draw
    AFTER INSERT 
    ON Drawing FOR EACH ROW
BEGIN 
    INSERT INTO Registry(enu_action, fk_id_usuario, fk_id_dibujo, var_fill_color, var_pen_color)
        VALUES("Creación", new.fk_id_usuario, new.id, (SELECT var_fill_color FROM Color), (SELECT var_pen_color FROM Color));

END$$

DELIMITER $$
CREATE TRIGGER tg_binnacle_update_draw
    AFTER UPDATE 
    ON Drawing FOR EACH ROW
BEGIN 
    INSERT INTO Registry (enu_action, fk_id_usuario, fk_id_dibujo, var_fill_color, var_pen_color)
        VALUES( "Modificación", new.fk_id_usuario, new.id, (SELECT var_fill_color FROM Color), (SELECT var_pen_color FROM Color) );

END $$

DELIMITER $$
CREATE TRIGGER tg_binnacle_delete_draw
    AFTER DELETE 
    ON Drawing FOR EACH ROW
BEGIN 
    INSERT INTO Registry (enu_action, fk_id_usuario, fk_id_dibujo, var_fill_color, var_pen_color)
        VALUES( "Eliminación", old.fk_id_usuario, old.id, (SELECT var_fill_color FROM Color), (SELECT var_pen_color FROM Color) );

END $$


DELIMITER ;



