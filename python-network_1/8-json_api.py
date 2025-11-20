#!/usr/bin/python3
"""
script take the url
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        try:
            result = response.json()
            if result:
                print(f"[{result.get('id')}] {result.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException:
        print("Not a valid JSON")
