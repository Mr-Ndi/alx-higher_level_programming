#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
"""
from urllib import request
from sys import argv
if __name__ == "__main__":
    link = sys.argv[1]
    w = urllib.request.Request(link)
    with urllib.request.urlopen(w) as ans:
        print(dict(ans.header).get('X-REQUEST-ID'))
