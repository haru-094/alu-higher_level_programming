#!/usr/bin/python3
"""
Fetch a URL and display the response body (utf-8). On HTTP errors print the status.
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            body = resp.read()
            print(body.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
