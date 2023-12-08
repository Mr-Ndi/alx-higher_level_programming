#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dlt = []
    for key, v in a_dictionary.items():
        if v == value:
            dlt.append(key)
    for i in dlt:
        del a_dictionary[i]
    return a_dictionary
