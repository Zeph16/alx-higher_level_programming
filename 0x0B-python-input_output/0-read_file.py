#!/usr/bin/python3
"""
Task 0 - Reading a text file with UTF-8 encoding
"""


def read_file(filename=""):
    """ Prints the contents of a file """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    print(data, end="")
