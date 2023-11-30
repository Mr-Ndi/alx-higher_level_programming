#!/usr/bin/python3
def remove_char_at(str, n):
    word = ""
    for i in range(0, len(str)):
        if i == n:
            pass
        else:
            word += str[i]
    return word
