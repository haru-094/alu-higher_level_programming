#!/usr/bin/python3
"""
Add command-line arguments to a JSON list file.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

FILENAME = 'add_item.json'


if __name__ == "__main__":
    try:
        my_list = load_from_json_file(FILENAME)
    except FileNotFoundError:
        my_list = []
    except ValueError:
        # invalid JSON content — start fresh
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, FILENAME)
