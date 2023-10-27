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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            ** dictionary: dictionary of an instance
        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """File to instances"""
        try:
            list_ret = []
            class_name = cls.__name__ + ".json"
            with open(class_name, mode="r") as file:
                list_ret_print = cls.from_json_string(file.read())
                for objt in list_ret_print:
                    list_ret.append(cls.create(**objt))
        except Exception:
            pass
        return list_ret
