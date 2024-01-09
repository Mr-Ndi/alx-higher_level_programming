#!/usr/bin/python3
"""adding all arguments to a Python list, and then save them to a file"""

import sys
from unicodedata import name

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file
    """ Load existing data from 'add_item.json' or initialize an empty list """
    file = "add_item.json"
    args = sys.argv[1:]
    try:
        lis = load(file)

    except FileNotFoundError:
        lis = []
    """ Add new arguments to the list"""
    lis.extend(args)
    """ Save the updated list back to 'add_item.json' """
    save(lis, file)
