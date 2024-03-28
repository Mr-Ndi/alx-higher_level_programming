#!/usr/bin/python3
""" send a request to the URL by requests nmodule"""
import requests
from sys import argv
if __name__ == "__main__":
    imy_url = argv[1]
    response = requests.get(imy_url)
    print(response.headers.get('X-Request-Id'))
