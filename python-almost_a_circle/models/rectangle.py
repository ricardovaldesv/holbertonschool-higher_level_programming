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

    def get_width(self):
        """Getter to obtain the width"""
        return self.__width

    def set_with(self, width):
        """Setter to update with"""
        self.__width = width

    def get_height(self):
        """Getter to obtain the height"""
        return self.__height

    def set_with(self, height):
        """Setter to update heihgt"""
        self.__width = height

    def get_x(self):
        """Getter to obtain x"""
        return self.__x

    def set_with(self, x):
        """Setter to update x"""
        self.__width = x

    def get_y(self):
        """Getter to obtain x"""
        return self.__y

    def set_y(self, y):
        """Setter to update y"""
        self.__width = y
