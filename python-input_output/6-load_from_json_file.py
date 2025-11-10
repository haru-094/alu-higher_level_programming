#!/usr/bin/python3
"""
load the json file
"""


import json

def load_from_json_file(my_obj, filename):
    """
    load the json file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
