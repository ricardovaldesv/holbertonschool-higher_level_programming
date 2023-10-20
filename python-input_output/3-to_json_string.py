#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)"""

import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)
        Args:
            my_obj : objet
        Return:
            JSON representation of an object (string)
        """
    return json.dumps(my_obj)
