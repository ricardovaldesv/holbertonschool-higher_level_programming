#!/usr/bin/python3
"""This file contain a class MyList that inherits of list"""


class MyList(list):
    """Class that MyList that inherits of list
        Args:
            obj (class): class parameter
    """
    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)
            Args:
                Dont have arguments
        """ 
        print(sorted(self))
