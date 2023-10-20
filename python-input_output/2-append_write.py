#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
        Args:
            filename : name of file
            text : text
        Return:
            the number of characters written
        """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
