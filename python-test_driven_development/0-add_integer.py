#!/usr/bin/python3
"""
Function that adds 2 integers hola.
a and b must be integers or floats, otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
