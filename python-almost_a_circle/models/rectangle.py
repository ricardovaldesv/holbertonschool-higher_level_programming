#!/usr/bin/python3
"""Firts Class Base"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter to obtain the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter to update with"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
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
        if height <= 0:
            raise ValueError("height must be > 0")
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
        if x < 0:
            raise ValueError("x must be >= 0")
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
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Function that return area"""
        return (self.__width * self.__height)

    def display(self):
        """Function that prints in stdout the Rectangle instance
        with the character # """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def display(self):
        """Function that prints"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args):
        """Function that assigns an argument to each attribute"""
        names = ["id", "width", "height", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
