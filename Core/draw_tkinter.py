# -*- coding: utf-8 -*-
import re
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom



class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)
    def getDict(self):
        d = {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "color": self.color,
            "command": "GoTo"
        }
        return d

    def __str__(self):

        d = '"x":%s,"y":%s,"width":%s,"color":"%s","command":"%s"'%(self.x, self.y, self.width, self.color, "GoTo")
        return d

class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)


    def __str__(self):
        d = '"radius":%s, "width":%s,"color":%s, "command:%s'%(self.radius, self.width, self.color,"Circle")
        return d
        #return '<Command radius="' + str(self.radius) + '" width="' + \
            #str(self.width) + '" color="' + self.color + '">Circle</Command>'


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        d = '"color:%s,command:%s"'%(self.color, "Inicio relleno")
        return d
        #return '<Command color="' + self.color + '">Inicio relleno </Command>'

class EndFillCommand:
    def __init__(self):
        pass
    
    def draw (self, turtle):
        turtle.end_fill()

    def __str__(self):
        d = '"command:%s"'%"Fin relleno"
        return d
        #return "<Command>Fin relleno</Commando"

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return '"command:%s"'% "Lápiz arriba"
        #return "<Command>Lápiz arriba</Commando"

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return '"command":%s'%"Lápiz abajo"
        #return "<Command>Lápiz abajo</Commando"

class PyList:
    def __init__(self):
        self.gcList = []

    def append(self, item):
        self.gcList = self.gcList + [item]

    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)

