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
    def width(self, value):
        """Setter to update with"""
        self.__width = value

    @property
    def height(self):
        """Getter to obtain the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to update heihgt"""
        self.__width = value

    @property
    def x(self):
        """Getter to obtain x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter to update x"""
        self.__width = value

    @property
    def y(self):
        """Getter to obtain x"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter to update y"""
        self.__width = value
