#!/usr/bin/python3
"""URL, sends request to the URL and displays the value of the X-Request-Id"""
from sys import argv
from urllib import request
if __name__ == "__main__":
    my_url = argv[1]

    with request.urlopen(my_url) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
