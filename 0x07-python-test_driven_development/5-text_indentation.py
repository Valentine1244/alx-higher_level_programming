#!/usr/bin/python3
"""
This module contains the function to print the string gievn and also
in the process adds two empty lines after any of these rejected strings
are encountered.

r_strings = ["?", ".", ":"].
"""
def text_indentation(text):
    """
    This function accepts only a string otherwise a TypeError is thrown
    and then prints the string adding two lines extra when either of
    the r_strings is encountered.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        r_strings = ["?", ".", ":"]
        index = 0
        while index < len(text):
            if index == 0:
                print(text[index], end="")
            else:
                if text[index - 1] in r_strings and text[index] == " ":
                    index += 1
                    continue
                else:
                    print(text[index], end="")
            for val in r_strings:
                if text[index] == val:
                    print()
                    print()
            if text[index] == " ":
                index += 1
            else:
                index += 1
