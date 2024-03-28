#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    link = sys.argv[1]
    with urllib.request.urlopen(link) as ans:
        print(dict((ans.header).get('X-REQUEST-ID')))
