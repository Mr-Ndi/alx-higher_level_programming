#!/usr/bin/usr/python3
def simple_delete(a_dictionary, key=""):

    sinye = a_dictionary.get(key)
    if sinye is not None:
        del a_dictionary[key]
    return a_dictionary
