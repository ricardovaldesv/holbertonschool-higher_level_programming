#!/usr/bin/python3
"""Firts Class Base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Calls the constructor of the base class (Rectangle)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return print"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """that assigns attributes:
            *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute"""
        names = ["id", "size", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Function that returns the dictionary representation of a Rectangle
        """
        names = ["id", "size", "x", "y"]
        value = [self.id, self.size, self.x, self.y]
        my_dict = dict(zip(names, value))
        return my_dict
