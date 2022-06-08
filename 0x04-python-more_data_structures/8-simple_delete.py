#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        keys = a_dictionary.keys()
        if key in keys:
            a_dictionary.pop(key)
    return a_dictionary
