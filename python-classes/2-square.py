#!/usr/bin/python3
"""Class Square that defines a square by: (based on 0-square.py)."""


class Square:
    """Private instance attribute: size."""
    def __init__(self, size=0):
        self.__size = int(size)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
