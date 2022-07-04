#!/usr/bin/python3
"""
Task 13 - Add Attribute
"""


def add_attribute(obj, key, value):
    """ Adds a new attribute to an object if possible """
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
