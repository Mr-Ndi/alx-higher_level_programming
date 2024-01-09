#!/usr/bin/python3
""" this will return an object that is represented by json string"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
