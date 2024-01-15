#!/usr/bin/python3


import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps("list_dictionaries")
