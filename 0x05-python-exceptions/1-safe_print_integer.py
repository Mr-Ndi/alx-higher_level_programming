#!/usr/bin/python3
def safe_print_integer(value):
    sign = True
    try:
        print("{:d}".format(value))
    except Exception:
        sign = False
    return sign
