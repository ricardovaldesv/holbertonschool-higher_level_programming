#!/usr/bin/python3
"""This file contain a function"""


def is_same_class(obj, a_class):
    """Method returns True if the object is exactly an instance
        of the specified class; otherwise False
        Args:
            obj is the object
        Return:
            True and false
    """
    return obj.__class__ is a_class
