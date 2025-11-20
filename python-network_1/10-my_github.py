#!/usr/bin/python3
"""
github auth script
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    response.raise_for_status()
    user_data = response.json()
    print(user_data.get("id"))
