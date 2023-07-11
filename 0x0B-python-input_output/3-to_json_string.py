#!/usr/bin/python3

"""
This module contains all a a function that returns the
JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    this accepts an object and then the function
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
