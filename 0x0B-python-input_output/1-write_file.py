#!/usr/bin/python3
"""
Task 1 - Writing to a file
"""


def write_file(filename="", text=""):
    """ Writes text into filename """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        chars = f.tell()
    return chars
