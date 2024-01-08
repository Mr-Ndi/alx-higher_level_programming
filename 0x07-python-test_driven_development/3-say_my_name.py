#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    message1 = "first_name must be a string"
    message2 = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(message1)
    if not isinstance(last_name, str):
        raise TypeError(message2)
    print("My name is {} {}".format(first_name, last_name))
