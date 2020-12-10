# -*- coding: utf-8 -*-
"""
@autor: Xenia Larissa Alfaro, Juan Carlos Boquin, Matt Saravia, Amilcar Antonio Rodriguez
@date: 2020/12/09
"""
import re
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
"""
El código de este modulo fue extraido del libro Data Structures and Algorithms with Python.
Edición: 2nd, 2015.
Autor: Kent D. Lee, Steve Hubbard
Editorial: Springer.
"""
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
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """

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
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """
        d = '"radius":%s, "width":%s,"color":%s, "command:%s'%(self.radius, self.width, self.color,"Circle")
        return d

class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """
        d = '"color:%s,command:%s"'%(self.color, "Inicio relleno")
        return d

class EndFillCommand:
    def __init__(self):
        pass
    
    def draw (self, turtle):
        turtle.end_fill()

    def __str__(self):
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """
        d = '"command:%s"'%"Fin relleno"
        return d

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """
        return '"command:%s"'% "Lápiz arriba"

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        """
        Se redefine el metodo __str__ para que retorne una cadena con formato de diccionario
        :return: String
        """
        return '"command":%s'%"Lápiz abajo"

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

