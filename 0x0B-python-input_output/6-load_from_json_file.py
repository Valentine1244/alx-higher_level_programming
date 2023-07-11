#!/usr/bin/python3

"""
This is a module that contains a function that creates an
Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function loads creates an Object from a “JSON file”
    """
    if type(filename) is str and filename is not None:
        with open(filename, encoding="UTF-8") as doc:
            r_file = doc.read()
            obj = json.loads(r_file)
            return obj
