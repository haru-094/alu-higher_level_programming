#!/usr/bin/python3
"""
load object form json
"""

import json


def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
