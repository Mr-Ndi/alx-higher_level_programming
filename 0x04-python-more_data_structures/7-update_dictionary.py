#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    sign = a_dictionary.get(key)
    if sign is not None:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
