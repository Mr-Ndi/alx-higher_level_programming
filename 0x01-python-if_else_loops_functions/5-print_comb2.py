#!/usr/bin/python3
for digit in range(0, 100):
    if digit != 99:
        print("{:02d}".format(digit), end=", ")
    else:
        print("{:02d}".format(digit))
