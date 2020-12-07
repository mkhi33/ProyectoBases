from Core.draw_tkinter import *
import json
import io
import os
from PIL import Image
from tkinter import simpledialog
from Core.DBManager import DBManager
from Core.MySqlEngine import MySqlEngine
from Core.ConnectionConfig import ConnectionConfig
class DrawingApplication(tkinter.Frame):
    def __init__(self, master=None, flag = None, contentDraw = None, isAdmin = True):
        super().__init__(master)
        self.idUser = -1
        self.idDraw = -1
        self.contentDraw = contentDraw
        self.flag = flag
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()
        self.database = DBManager()
        self.isAdmin = isAdmin
        self.count = 0
    def buildWindow(self):
        self.master.title("Draw")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)
        def newWindow():
            theTurtle.pen()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()
        fileMenu.add_command(label="New", command=newWindow)
        def loadDraw(file):
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



        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)
            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName("Command")
            for commandElement in graphicsCommands:

                command = commandElement.firstChild.data.strip()

                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x, y, width, color)
                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius, width, color)
                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)
                elif command == "EndFill":
                    cmd = EndFillCommand()
                elif command == "PenUp":
                    cmd = PenUpCommand()
                elif command == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Comando desconocido " + command)

                graphicsCommands.append(cmd)

        def loadFile(filename = ""):
            newWindow()
            if(self.flag != 'edit'):
                self.graphicsCommands = PyList()
            loadDraw(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()

        fileMenu.add_command(label="Cargar...", command=loadFile)

        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title="Selecciona una")

            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0, 0, 1, "#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()

            #parseJson(filename)
            #parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()
        def downloadJson():
            filename = tkinter.filedialog.asksaveasfilename(title="Guardar JSON como...")
            if(filename != ""):
                write(filename)

        fileMenu.add_command(label="Descargar JSON", command=downloadJson)


        def writeJson(filename):
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



        def saveFile():
            fileName = simpledialog.askstring("Input", "Guardar como...")

            if(fileName):
                writeJson(fileName)


        fileMenu.add_command(label="Guardar como...", command=saveFile)

        fileMenu.add_command(label="Salir", command=self.master.destroy)

        bar.add_cascade(label="File", menu=fileMenu)

        self.master.config(menu=bar)


        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)

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

        penColor.set("#000000")

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
        fillColor.set("#000000")

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
        def configure():
            pass
        def saveImg():
            #self.master.withdraw()
            ps = screen.getcanvas().postscript( colormode = 'color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.show("Dibujo")

        if(self.flag == "edit"):
            loadFile(self.contentDraw)
        elif self.flag == "view":
            print("Show")
            loadFile(self.contentDraw)
            saveImg()

        screen.onkeypress(undoHandler, "u")
        screen.listen()

