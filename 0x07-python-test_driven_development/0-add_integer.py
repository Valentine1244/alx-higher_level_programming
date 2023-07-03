#!/usr/bin/python3
"""
This is a Module to add two different numbers together. They can either
be a float or an int and returns the sum. It also checks for common errors
and throws them
"""


def add_integer(a, b=98):
    """
    This accepts two values a & b and returns their sum. b has been initialized
    by default. Although, it can also be re-initialized.

    The function checks if values give are either float, or a non-int value.
    if float, it converts it to an int else throws a ValueError exception if
    otherwise
    """
    if type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
