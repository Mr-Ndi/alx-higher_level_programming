#!/usr/bin/python3
import request
if __name__ == "__main__":
    data = request.ge('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))
