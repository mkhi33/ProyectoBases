#-*-coding:utf-8 -*-

"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
@versión 1.0
"""
from Core.draw_tkinter import *
import json
import io
from PIL import Image
from tkinter import simpledialog, messagebox
from Core.DBManager import DBManager
from PyQt5.QtCore import QThread, pyqtSignal, QBasicTimer
from Core.guiDraw import GuiDraw
class DrawingApplication(tkinter.Frame):
    """
    Esta clase maneja una ventana de tkinter mediante la cual se puede dibujar, editar, eliminar dibujos
    """

    def __init__(self, master=None, flag = None, contentDraw = None, isAdmin = False, penColor = "#000000", fillColor = "#000000", idUser = -1, idDraw = -1 ):
        """
        @name: __init__
        @param master: objeto tkinter.TK()
        @param flag: Bandera (edit, view, save) segun la acción que realiza el usuario.
        @param contentDraw: contenido en cadena String en formato JSON del contenido del dibujo.
        @param isAdmin: Booleano que indica si el usuario es administrador.
        @param pencColor: Color del lapiz.
        @param fillColor: color fillcolor.
        @param idUser: id de usuario
        @param idDraw: id del dibujo.
        """
        super().__init__(master)
        self.idUser = idUser
        self.idDraw = idDraw
        self.contentDraw = contentDraw
        self.flag = flag
        self.pack()
        self.uiDraw = GuiDraw()
        self.reload = 'load'
        self.graphicsCommands = PyList()
        self.database = DBManager()
        self.isAdmin = isAdmin
        self.count = 0
        self.penColor = penColor
        self.fillColor = fillColor
        self.buildWindow()

    def buildWindow(self):
        """
        @name: buildWindow
        @param: no recibe parametros.
        @description: Construye la ventana grafica del dibujo.
        """
        self.master.title("Draw")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        def newWindow():
            """
            @name newWindow
            @param: no recibe parametros.
            @description: Función interna que genera una nueva ventana.
            """
            theTurtle.pen()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()
        def cleanWindow():
            """
            @name: cleanWindow
            @param: no recibe parametros.
            @description limpia la ventana de dibujo destruyéndola.
            """
            self.reload = 'new'
            self.master.destroy()
        fileMenu.add_command(label="Nuevo", command=cleanWindow)

        def loadDraw(file):
            """
            @name loadDraw
            @param file: contenido del dibujo en String
            @description: Carga un dibujo desde un string con formato de diccionario.
            @return: No retorna.
            """
            data = json.loads(file)
            for i in range(len(data.items())):

                if(data["%s"%i]["command"] == "GoTo"):
                    x = float(data["%s"%i]["x"])
                    y = float(data["%s"%i]["y"])
                    width = float(data["%s"%i]["width"])
                    color = data["%s"%i]["color"]
                    cmd = GoToCommand(x,y,width, color)
                elif data["%s"%i]["command"] == "Circle":
                    radius = float(data["%s"%i]["radius"])
                    width = float(data["%s"%i]["width"])
                    color = data["%s"%i]["color"]
                    cmd = BeginFillCommand(radius, width,color)
                elif data["%s"%i]["command"] == "BegiFill":
                    color = data["%s"%i]["color"]
                    cmd = BeginFillCommand(color)
                elif data["%s"%i]["command"] == "EndFill":
                    cmd = EndFillCommand()
                elif data["%s"%i]["command"] == "PenUp":
                    cmd = PenUpCommand()
                elif data["%s"%i]["command"] == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Comando desconocido "+data["%s"%i]["command"] )
                self.graphicsCommands.append(cmd)

        def loadFile(filename = ""):
            """
            @name: loadFile
            @param fileName: nombre de arcivo
            @description: Carga un dibujo a partir de un archivo
            @return No retorna.
            """
            newWindow()
            if(self.flag != 'edit'):
                self.graphicsCommands = PyList()
            loadDraw(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()

        def loadFromDataBase():
            """
            @name: loadFromDataBase
            @param: No recibe parametros.
            @description: asigna una bandera de carga de archivo.
            """
            self.reload = 'load'
            self.master.destroy()

        def on_closing():
            """
            @name: on_closing
            @param: No recibe parametros.
            @description: muestra un  dialogo de confirmación, en caso de aceptar se cerrara la ventana, de lo contrario permanecera en ella.
            @return: No retorna.

            """
            if messagebox.askokcancel("Salir", "¿Quiere salir?"):
                self.reload = 'close'
                self.master.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)

        if(self.isAdmin):
            fileMenu.add_command(label="Cargar...", command=loadFromDataBase)

        def downloadJson():
            """
            @name: downloadJson
            @param: No recibe parametros.
            @description: Descarga el dibujo en un archivo JSON.
            """
            filename = tkinter.filedialog.asksaveasfilename(title="Guardar JSON como...")
            if(filename):
                saveJson(filename)


        fileMenu.add_command(label="Descargar JSON", command=downloadJson)


        def writeJson(filename):
            """
            @name: writeJson
            @param: fileName
            @description: Guarda el JSON dentro de la base de datos.
            @return: No retorna.
            """
            j = {}
            count = 0


            if self.flag == 'save':
                for cmd in self.graphicsCommands:
                    j[count] = cmd.getDict()
                    count += 1

                self.database.saveDraw(filename,json.dumps(j),self.idUser)
            elif self.flag == 'edit':
                self.contentDraw = json.loads(self.contentDraw)
                self.count = len(self.contentDraw) - 1
                for cmd in self.graphicsCommands:
                    self.contentDraw[self.count] = cmd.getDict()
                    self.count += 1

                self.database.editDraw(filename, json.dumps(self.contentDraw), self.idUser, self.idDraw)

        def saveJson(filename):
            """
            @name: saveJson
            @param fileName: Nombre del archivo.
            @description: Guarda un archivo en el disco duro según la ruta especificada.
            @return: No retorna.
            """
            try:
                content = json.loads( self.database.getDrawingB(self.idDraw)[0][0])
                with open(filename, 'w') as file:
                    json.dump(content, file, indent=4)
            except:
                pass



        def saveFile():
            """
            @name saveFile
            @param: No recibe parametros.
            @description: llama a la función writeJson y guarda el archivo según la ruta especificada por el usuario.
            @return: No retorna.
            """
            fileName = simpledialog.askstring("Input", "Guardar como...")

            if(fileName):
                writeJson(fileName)

        fileMenu.add_command(label="Guardar como...", command=saveFile)

        def configuration():
            """
            @name: configuration
            @param: no recibe parametros.
            @description: Asigna la bandera reload en 'config'lo que hace que se abra la ventana qt5 en modo config.
            @return No retorna
            """
            self.reload = 'config'
            self.master.destroy()
        
        """
        Si es administrador se visualizara un boton 'Configurar' en el menu File 
        """
        if self.isAdmin:
            fileMenu.add_command(label = "Configurar", command = configuration)


        fileMenu.add_command(label="Salir", command=on_closing)

        bar.add_cascade(label="File", menu=fileMenu)
        self.master.config(menu=bar)


        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)
        # Hasta aquí
        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.pencolor(self.penColor)
        theTurtle.fillcolor(self.fillColor)
        if self.flag == "view":
            self.master.withdraw()
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()


        screen.tracer(0)


        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        pointLabel = tkinter.Label(sideBar, text="Width")
        pointLabel.pack()

        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar, textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()


        """
        Funciones desde aquí son obtenidas del libro.
        Data Structures and Algorithms with Python.
        """
        def circleHandler():
            cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            screen.update()
            screen.listen()

        circleButton = tkinter.Button(sideBar, text="Dibujar círculo", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)

        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Color del lápiz")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()

        penColor.set(self.penColor)

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])

        penColorButton = tkinter.Button(sideBar, text="Selecciona un color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)
        fillLabel = tkinter.Label(sideBar, text="Llenar color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar, textvariable=fillColor)
        fillEntry.pack()
        fillColor.set(self.fillColor)

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9:-2])

        fillColorButton = \
            tkinter.Button(sideBar, text="Escoja color de relleno", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text="Inicio relleno", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = tkinter.Button(sideBar, text="Terminar relleno", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Lápiz abajo")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Lápiz arriba")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text="Lápiz arriba", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Lápiz abajo")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text="Lápiz abajo", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)

        def clickHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(clickHandler)

        def dragHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()
        def saveImg():
            """
            @name: saveImg
            @param: No recibe parametros.
            @description: Visualiza una imagen segun el dibujo seleccionado.
            @return: No retorna.
            """
            ps = screen.getcanvas().postscript( colormode = 'color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.show("Dibujo")
            self.database.setVisualitation(self.idDraw, self.idUser, self.fillColor, self.penColor)


        """
        Sí se esta editando un dibujo se genera el dibujo en la pantalla segun el contenido recuperado de la base de datos.

        Si esta visualizando se genera el dibujo en una pequeña ventana a partir de l contenido recuperado de la base de datos.
        """
        if(self.flag == "edit"):
            loadFile(self.contentDraw)
        elif self.flag == "view":

            loadFile(self.contentDraw)
            saveImg()

            screen.onkeypress(undoHandler, "u")
        screen.listen()


