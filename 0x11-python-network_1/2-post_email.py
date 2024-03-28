#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to it.

Usage: ./2-post_email.py <URL><Email>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
