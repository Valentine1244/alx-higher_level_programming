#!/usr/bin/python3
from models.base import Base


"""
This file contains the class for the rectangle class
"""


class Rectangle(Base):
    """
    This is the rectangle class which inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width width must be > 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height width must be > 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} \
- {}/{}".format(self.id, self.__x, self.__y,
                self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Finds the area
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints the visual of the object
        """
        for space in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the value of the rectangle
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        if len(args) == 0 and len(kwargs) > 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Converts the object to a dictinoary
        """
        return {"x": self.x, "y": self.y,
                "id": self.id, "height": self.height, "width": self.width}
