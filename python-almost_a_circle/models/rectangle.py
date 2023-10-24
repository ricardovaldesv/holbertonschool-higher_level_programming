#!/usr/bin/python3
"""Firts Class Base"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Getter to obtain the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter to update with"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter to obtain the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter to update heihgt"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Getter to obtain x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter to update x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Getter to obtain x"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter to update y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y
