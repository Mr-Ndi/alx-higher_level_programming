#!/usr/bin/python3
import urllib.request
from sys import argv
if __name__ == "__main__":
    link = sys.argv[1]
    with urllib.request.urlopen(link) as ans:
        print(dict((ans.header).get('X-REQUEST-ID')))
