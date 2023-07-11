#!/usr/bin/python3

"""
This module contains a function that writes an Object to a
text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function saves a json object to a file
    """
    if type(filename) is str and filename is not None:
        with open(filename, mode="w", encoding="UTF-8") as doc:
            doc.write(json.dumps(my_obj))
