#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    names = dir(hidden_4)
    for i in names:
        if not i.startswith("__"):
            print(i)
