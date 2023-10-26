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
        """save_to_file method that writes the json string representation of
        list_obts to a file.

        Args:
            list_objs ([list of objects]): list of cls instances
        """
        list_dicts_python = []
        class_name = cls.__name__ + ".json"
        if list_objs is not None:
            for lst in list_objs:
                list_dicts_python.append(lst.to_dictionary())
        with open(class_name, "w+", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(list_dicts_python))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string: list of the JSON string
        """

        if json_string is not () and json_string is not None:
            return json.loads(json_string)
        else:
            dictionaries = []
            return dictionaries
