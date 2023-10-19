#!/usr/bin/python3
"""This file contain a class empty"""


class BaseGeometry:
    """class empty
    """
    def area(self):
        """function that raises an Exception with the message area()
            is not implemented You are not allowed to import any module
        Args:
            emty
        Return:
            Nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that raises an Exception with the message area()
            is not implemented
            You are not allowed to import any module
            Args:
                emty
            Return:
                Nothing
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""This file contain a class Rectangle that inherits of BaseGeometry"""


class Rectangle(BaseGeometry):
    """function
        """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = int(width)
        self.__height = int(height)
