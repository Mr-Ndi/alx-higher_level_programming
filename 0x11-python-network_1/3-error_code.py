#!/usr/bin/python3
import urllib.error
import urllib.response
import sys
""" script that takes in a URL, sends a request
    to the URL and displays the body of the response
    usage ././3-error_code.py <URL>
"""
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.urlopen(url) as ans:
            print(ans.read().decode("utf-8"))
    except:
        print("Error code: {}".format(error.HTTPError.code))
