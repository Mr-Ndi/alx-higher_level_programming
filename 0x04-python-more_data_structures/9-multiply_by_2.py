#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new = a_dictionary.copy()
    for ke in new:
        new[ke] = new[ke] * 2
    return new
