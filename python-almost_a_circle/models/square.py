#!/usr/bin/python3
"""Firts Class Base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Calls the constructor of the base class (Rectangle)"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        self.__width = size
        self.__height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
