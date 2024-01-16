#!/usr/bin/python3
"""Defines a base model class."""

import json


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns JSON string representation
            from python dictionary form to json dictionary form
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """A class method that writes Json string to a filea
            by taking the the list of dictionary and turn them into json
            form and save them
        """

        name = cls.__name__+".json"
        with open("name", "w") as dd:
            if list_objs is None:
                dd.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                dd.write(Base.to_json_string(list_dicts))
