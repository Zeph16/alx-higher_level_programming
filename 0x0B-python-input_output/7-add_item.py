#!/usr/bin/python3
"""
Task 7 - Add arguments and Save to file
"""
import sys
import os


args = sys.argv[1:]

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

items = []
if os.path.exists('add_item.json'):
    items = load_JSON('add_item.json')

save(items + args, "add_item.json")

