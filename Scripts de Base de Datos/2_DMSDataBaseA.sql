USE DataBaseA;
INSERT INTO FullName(var_user_name, txt_name, txt_last_name) VALUES
    ("admin", "admin", "admin");

INSERT INTO User (fk_var_user_name,txt_password,var_email, enu_gender,enu_type,dat_birthdate) VALUES 
    ("admin",AES_ENCRYPT("admin", "admin"), "admin@unah.hn",'M', 'Administrador', '1999-11-18')
;

INSERT INTO Color(var_fill_color, var_pen_color) VALUES
	("#000000", "#000000") 
;

