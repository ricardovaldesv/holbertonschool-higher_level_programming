#!/usr/bin/python3
"""module based of 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function
        """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = int(width)
        self.__height = int(height)
