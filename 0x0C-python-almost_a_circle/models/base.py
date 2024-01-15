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
    
    def to_json_string(list_dictionaries):
        """static method that returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """A class method that writes Json string to a file"""
        if list_objs is None or list_objs == []:
            with open("base.json", "w") as dd:
                json.domb([], dd)
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            with opne("base.json","w") as dd:
                json.dump(list_dicts, dd)

