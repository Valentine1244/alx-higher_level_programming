#!/usr/bin/python3

"""
This is a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This function writes a text to a file and
    returns the number of characters
    """
    text_written = 0

    if filename is not None:
        with open(filename, mode="w", encoding="UTF-8") as new_file:
            text_written = new_file.write(text)
    return text_written
