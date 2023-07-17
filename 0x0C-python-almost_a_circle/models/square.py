#!/usr/bin/python3

from models.rectangle import Rectangle


"""
This is a module containing the code for the Square class.
"""


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class which then
    inherits from the Base class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.height = value
            self.width = value

    def update(self, *args, **kwargs):
        """
        Updates the value of the Square
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
            self.height = args[1]
        if len(args) >= 4:
            self.x = args[2]
        if len(args) >= 5:
            self.y = args[3]
        if len(args) == 0 and len(kwargs) > 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Converts the object to a dictinoary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
