#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""This file contain a class empty"""


class Rectangle(BaseGeometry):
    """function
        """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = int(width)
        self.__height = int(height)
