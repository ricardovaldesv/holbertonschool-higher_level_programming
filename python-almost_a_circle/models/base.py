#!/usr/bin/python3
"""Firts Class Base"""
import json


class Base:
    """This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Function that returns the JSON string representation
            of list_dictionaries"""

        if list_dictionaries is not () and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            list_dictionaries = []
            return list_dictionaries
