#!/usr/bin/python3
"""creating an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """ A function that creates an Object from a json file """
    with open(filename, 'r') as pat:
        return json.load(pat)
