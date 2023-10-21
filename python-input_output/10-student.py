#!/usr/bin/python3
"""Module defines a student by first_name, last_name, age
"""


class Student:
    """class defines a student by first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function
        """
        if attrs is None:
            return self.__dict__
        selected_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                selected_attrs[attr] = getattr(self, attr)
        return selected_attrs
