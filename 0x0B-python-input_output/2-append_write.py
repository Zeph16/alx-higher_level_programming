#!/usr/bin/python3
"""
Task 2 - Append to a file
"""


def append_write(filename="", text=""):
    """ Appends text to filename """
    with open(filename, 'a', encoding="utf-8") as f:
        chars = f.write(text)
    return chars
