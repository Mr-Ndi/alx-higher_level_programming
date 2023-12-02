#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for char in my_string:
        if char not in {'c', 'C'}:
            newstring += char
    return newstring
