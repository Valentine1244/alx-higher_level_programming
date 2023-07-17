#!/usr/bin/python3
import json

"""
This is a file for the base class
"""


class Base:
    """
    This is the base class for the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts Json object to the str representation
        """
        if type(list_dictionaries) is list and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the list_objs to file
        """
        if type(list_objs) is list:
            with open(cls.__name__+".json", mode="w") as newfile:
                newfile.write(cls.to_json_string(
                    [x.__getattribute__("to_dictionary")()
                        for x in list_objs if type(x) is cls]))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts json String to Json Object
        """
        if type(json_string) is str and json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads json from file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                return [cls.create(**data) for data in dict_list]
        except FileNotFoundError:
            return []
