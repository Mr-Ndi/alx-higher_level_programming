#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as ans:
    data = ans.read()
    real_data = data.decode('utf-8')
    lines = real_data.split('\n')
    for line in lines:
        print("-{}".format(line))
