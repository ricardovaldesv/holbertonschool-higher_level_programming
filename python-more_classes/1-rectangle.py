#!/usr/bin/python3
"""Represent a clas Rectangle."""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.heiht = height
    
    def width(self):
        return self.__with
    
    def width(self, value):
        if type(value) is not int:
            raise TypeError ("width must be an integer")
        if value < 0:
            raise ValueError ("width must be >= 0")
        self.__width = value
    
    def height(self):
        return self.__with
    
    def height(self, value):
        if type(value) is not int:
            raise TypeError ("height must be an integer")
        if value < 0:
            raise ValueError ("height must be >= 0)
        self.__width = value



    
    