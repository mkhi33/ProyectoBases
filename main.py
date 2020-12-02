from Core.draw_tkinter import *
#from Core.DrawProgram import *
def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("Ejecución completada")

if __name__ == "__main__":
    main()
