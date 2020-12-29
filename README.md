Documentación Proyecto Base de Datos I IIIPAC-2020 UNAH
=========================
- @author Larissa Alfaro, Juan Boquín, Amilcar Rodriguez, Matt Saravia
- @date 2020/08/18

# **Instalar dependencias**
- En la carpeta raiz existe un archivo 'requeriments.txt'
- Dentro de la carpeta raiz en una termina ejecutar el siguiente comando:


		pip3 install -r requeriments.txt
	

- El comando anterior instalara las dependencias necesarias para ejecutar el programa.

# **SQL**

## **Base de Datos**
* Lluvia de ideas:
    1. Tuvimos la idea de que los userName y los email sean únicos en la tabla user.
    2. Que los nombres estén separados en otra tabla con los campos de nombre y apellido para implementar la formalización
    3. Previa investigación del tipo de dato blob en MySql para la previa comprensión e implementación en la base de datos.

* Problemas encontrados:
    1. Tuvimos un error con el uso de CONSTRAINT al incluir un campo con un tipo de dato TEXT.
   
		***Cambiamos el tipo de dato a VARCHAR, para resolver el problema.***
    1. En el uso de llaves foraneas y hacer una referencia hacia la otra tabla, encontramos un error que no podía hacer la referencia de los campos.
   
		***Ya que en una tabla la llave foranea era de un tipo de dato diferente al de la referencia, se le cambio el tipo de dato para que los dos fueramos iguales.***

### **Desarrollo**


### **Diagrama Entidad Relación**
![Imagen](https://fotos.subefotos.com/000f5b26935c3e65b5c6e6a137b07913o.png) 

### **Actualización al diagrama de Entidad Relación con el formato final de las tablas que necesitamos para nuestra base de datos.**
![Imagen](https://fotos.subefotos.com/a98e56f31a02adce32f5caf13d865bd0o.png) 


 
    

# **Python**

## **Código**
* Lluvia de ideas:
    1. La investigación previa de los componentes que se utilizarán para los diferentes métodos para el CRUD.

* Problemas encontrados:
    1. Al momento de crear nuevos usuarios, no se lograba insertar los datos a la tabla.
   
		***La solución del problema era que nos faltaba 1 línea de código que sirve para lograr insertar los datos a la tabla. 
		.commit()***
    1. Al momento de editar un dibujo, se sobreescribía sobre el dibujo editado.
		
		***Convertimos la cadena con el json.loads, utilizando un for fuimos iterando para ir agregando las nuevas coordenadas al json original***


## **Tkinter**
* Lluvia de ideas:
    1. Comprensión y análisis del código extraído del libro "Data Structures and Algorithms with Python" 


### **Desarrollo**

Ya que el archivo resultante del algoritmo era un XML, debíamos convertirlo a JSON, para esto, primeramente analizamos el código para encontrar las zonas del código donde se encontraba la creación del XML, seguidamente observamos que el XML se creaba a partir de strings con el formato especifico, así que proseguimos a realizar los cambios necesarios en el código para cambiar la estructura a JSON y obtener como archivo final un JSON.

## **PyQT5**
* Lluvia de ideas:
    1. Desactivar desde la interfaz los campos que no son requeridos para el administrador para modificar.
    2. Ocultar botones que no son requeridos en la interfaz y mostrarlos cuando sean requeridos.
    3. Mostrar ventanas de confirmación y alertas.

* Problemas encontrados:
    1. Encontramos un problema al momento de querer obtener los datos individuales de la fecha de nacimiento. 
  
		***Utilizamos los métodos day(), year() y month() de QT5 para poder obtenerlos.***
    1. No podíamos desactivar el modificar elementos dentro de la lista.
   
		***Utilizabamos un método desconocido, entonces utilizamos el método setFlags para lograr la solución.***


### **Desarrollo**

Primero realizamos un diseño para tener una idea de como haremos nuestras ventanas, que opciones debe contener dentro de ellas.

Utilizamos el diseñador de ventanas de qt5 para desarrollar de manera rápida los scripts de python sin tener que escribir código, para convertir los archivos .ui a .py mediante linux usamos el siguiente comando:

    pyuic5 ventana.ui > ventana.py

El comando anterior permite compilar el archivo.ui a un script .py que python puede entender.

Para entender el funcionamiento de pyqt5 y ademas para obtener ayuda acudimos a la documentación del QT5 para python mediante la siguiente pagina:

    https://doc.qt.io/qtforpython/

### **Diseño de ventanas**

![Imagen](https://fotos.subefotos.com/09fb83e794e475862bf49df6d5a0144fo.jpg) 

![Imagen](https://fotos.subefotos.com/62115f6077a9b2d3a7c3b3019206716eo.jpg) 



