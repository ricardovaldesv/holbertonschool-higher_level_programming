#!/usr/bin/python3
"""Function that open a text file"""


def read_file(filename=""):
    """function that open a text file
        Args:
            name of file
        Return:
            Nothing
        """
    with open(filename, encoding="utf-8") as file:
        file1 = file.read()
        for line in file1:
            print(line, end='')
