#!/usr/bin/python3
import urllib.request
import sys
link = sys.argv[1]
with urllib.request.urlopen(link) as ans:
    data = ans.getheader('X-REQUEST-ID')
    print(data)
