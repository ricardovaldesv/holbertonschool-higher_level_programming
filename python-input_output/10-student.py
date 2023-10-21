#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        selected_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                selected_attrs[attr] = getattr(self, attr)
        return selected_attrs
