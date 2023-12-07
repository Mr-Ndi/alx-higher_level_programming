#!/usr/bin/usr/python3
def simple_delete(a_dictionary, key=""):

    if key in set(list(a_dictionary)):
        del a_dictionary[str(key)]
    return a_dictionary
