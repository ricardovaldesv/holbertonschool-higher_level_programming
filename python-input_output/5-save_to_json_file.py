#!/usr/bin/python3
"""Function that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):

    """Function that writes an Object to a text file, using a JSON
        representation
        Args:
            my_obj : string
            filename : file name
        Return:
            text file
        """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(json.dumps(my_obj))
