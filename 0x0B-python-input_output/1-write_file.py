#!/usr/bin/python3
"""this one will deal with writting on a file
    but also we will focus on counting number of the characters written on it
"""


def write_file(filename="", text=""):
    """ a function to overwrite or create but also count appended characters"""
    size = 0
    with open(filename, 'w') as file:
        for char in text:
            file.write(char)
            size += 1
    return size
