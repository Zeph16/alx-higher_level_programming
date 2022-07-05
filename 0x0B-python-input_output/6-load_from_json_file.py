#!/usr/bin/python3
"""
Task 6 - From JSON to Object
"""
import json


def load_from_json_file(filename):
    """ Returns Object from JSON """
    with open(filename, 'r') as f:
        return json.load(f)
