#!/usr/bin/python3

"""
This module contains the a a function that appends a string at the
end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    The function takes filename and text then appends the file
    """
    appended = 0

    if filename is not None:
        with open(filename, mode="a", encoding="UTF-8") as new_file:
            appended = new_file.write(text)
    return appended
