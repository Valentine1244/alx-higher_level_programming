#!/usr/bin/python3

"""
This module contains a script that adds all arguments
to a Python list, and then save them to a file
"""


if __name__ == "__main__":
    import sys
    from json import JSONDecodeError

    savetojson = __import__("5-save_to_json_file").save_to_json_file
    loadtojson = __import__("6-load_from_json_file").load_from_json_file

    args = sys.argv[1:]

    try:
        loaded_json = loadtojson("add_item.json")
    except (FileNotFoundError, JSONDecodeError):
        loaded_json = []

    arguments = args + loaded_json
    savetojson(arguments, "add_item.json")
