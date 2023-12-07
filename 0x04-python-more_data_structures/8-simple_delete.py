#!/usr/bin/usr/python3
def simple_delete(a_dictionary, key=""):

    new = a_dictionary.copy()
    if key in new:
        del new[key]
    return new
