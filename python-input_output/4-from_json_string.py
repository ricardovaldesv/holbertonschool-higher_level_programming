#!/usr/bin/python3
"""Function that returns an object (Python data structure)
    represented by a JSON string:"""

import json


def from_json_string(my_str):

    """Function that returns an object (Python data structure)
        represented by a JSON string:
        Args:
            my_str : string
        Return:
            objet python
        """
    return json.loads(my_str)
