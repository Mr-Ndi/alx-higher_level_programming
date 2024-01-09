#!/usr/bin/python3
""" this will return an object that is represented by json string"""
import json


def from_json_string(my_str):
    """ tis is the one to convert a json object into a string"""
    return json.loads(my_str)
