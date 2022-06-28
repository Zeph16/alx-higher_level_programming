#!/usr/bin/python3
"""
Class can't be instantiated dynamically
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
