#!/usr/bin/python3

"""
    This module contains the code to accept a user's name and then
    prints out the person's to stdout.

    Only two arguments are required, the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    This function accepts the first and last name string then outputs
    it to Stdout. The function checks for arguments that is not string
    and then throws an error
    """
    if first_name is None:
        raise TypeError("first_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    elif type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
