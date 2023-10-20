#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
        Args:
            filename : name of file
            text : text
        Return:
            the number of characters written
        """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
