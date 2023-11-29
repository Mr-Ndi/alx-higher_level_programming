#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    result = []
    for n1 in range(length):
        char = ord(str[n1])
        if char >= 97 and char < 123:
            charac = chr(char - 32)
        else:
            charac = chr(char)
        print("{}".format(charac), end='')
    print()
