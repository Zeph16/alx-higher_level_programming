#!/usr/bin/python3
"""
Task 5 - Saving an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Saves object json string to file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
