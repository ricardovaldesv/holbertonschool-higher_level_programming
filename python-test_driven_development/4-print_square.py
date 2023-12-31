#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size != 0:
        for i in range(0, size):
            for j in range(0, size):
                print("{}".format("#"), end="")
            if i < size - 1:
                print("")
        print("")
