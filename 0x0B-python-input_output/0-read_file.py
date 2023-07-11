#!/usr/bin/python3

"""
This file contains the module of a function that reads a
text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a file name and prints to stdout
    """
    if filename is not None:
        with open(filename, encoding="UTF-8") as newfile:
            print(newfile.read(), end="")
