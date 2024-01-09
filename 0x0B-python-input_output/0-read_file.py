#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as p:
        cont = p.read()
        print(cont, end="")
