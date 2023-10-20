#!/usr/bin/python3
"""module based of 9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """function
        """

    def __init__(self, size):
        """function
            """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """function
        """
        return self.__size * self.__size

    def __str__(self):
        """function
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
