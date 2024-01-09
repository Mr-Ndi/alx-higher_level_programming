#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """ a function that will load a json object into a file """
    with open(filename, "w") as p:
        json.dump(my_obj, p)
