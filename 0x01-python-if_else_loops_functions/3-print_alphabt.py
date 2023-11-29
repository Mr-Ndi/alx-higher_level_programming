#!/usr/bin/python3
for charac in range(97, 123):
    if charac == 101 or charac == 113:
        continue
    print("{}".format(chr(charac)), end="")
