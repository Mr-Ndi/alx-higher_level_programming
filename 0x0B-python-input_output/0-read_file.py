#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='UTF-8') as p:
            cont = p.read()
            print(cont)
    except FileNotFound:
        print("file not found")
    except UnicodeDecodeError:
        print("unable to decode the file")
