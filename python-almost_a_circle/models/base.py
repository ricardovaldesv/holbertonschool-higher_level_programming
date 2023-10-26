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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the JSON string representation
            of list_dictionaries"""

        if list_dictionaries is not () and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            list_dictionaries = "[]"
            return list_dictionaries

    @classmethod
    def save_to_file(cls, list_objs):

        dictionary1 = list_objs[0].to_dictionary()
        json_dictionary1 = Base.to_json_string([dictionary1])

        dictionary2 = list_objs[1].to_dictionary()
        json_dictionary2 = Base.to_json_string([dictionary2])

        filename = cls.__name__

        with open(filename, mode='w', encoding='utf-8') as a_file:
            return a_file.write("[" + (str(dictionary1))
                                + ", " + str(dictionary2) + "]")
