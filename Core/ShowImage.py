from Core.draw_tkinter import *
import json
import io
from PIL import Image
from tkinter import simpledialog
from Core.DBManager import DBManager

class ShowImage(tkinter.Frame):
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

        def loadFile(filename = ""):

            if(self.flag != 'edit'):
                self.graphicsCommands = PyList()
            loadDraw(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(turtle)

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





        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)
        # Hasta aquí

        def saveImg():
            #self.master.withdraw()
            ps = canvas.postscript( colormode = 'color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.show("Dibujo")


