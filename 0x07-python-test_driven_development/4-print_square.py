#!/usr/bin/python3

"""
This Module contains the code for printing # for a number of
time specified by the user.

The argunment must be an int only else an exception is raised
"""


def print_square(size):
    """
    This is the function to print the sqaure specified by
    a number of times (size) by the user
    """
    chk = 0
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        while chk < size:
            print("#" * size)
            chk += 1
