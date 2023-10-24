#!/usr/bin/python3
"""Firts Class Base"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter to obtain the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter to update with"""
        self.__width = width

    @property
    def height(self):
        """Getter to obtain the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter to update heihgt"""
        self.__height = height

    @property
    def x(self):
        """Getter to obtain x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter to update x"""
        self.__x = x

    @property
    def y(self):
        """Getter to obtain x"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter to update y"""
        self.__y = y
