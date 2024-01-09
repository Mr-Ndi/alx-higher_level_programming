#!/usr/bin/python3
"""this one will deal with writting on a file
    but also we will focus on counting number of the characters written on it
"""


def append_write(filename="", text=""):
    """ a function to append characters"""
    size = 0
    with open(filename, 'a') as file:
        for char in text:
            file.write(char)
            size += 1
    return size
