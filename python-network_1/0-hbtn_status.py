#!/usr/bin/python3
"""
Fetches the url and display the respond
"""

from urllib import request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- " + body.decode('utf-8'))
