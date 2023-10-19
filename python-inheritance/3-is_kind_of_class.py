#!/usr/bin/python3
"""This file contain a function"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False.
        Args:
            obj is the object
            a_class is the class
        Return:
            True and false
    """
    return isinstance(obj, a_class)
