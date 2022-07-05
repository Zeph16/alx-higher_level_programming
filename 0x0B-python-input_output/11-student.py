#!/usr/bin/python3
"""
Task 11 - Student JSON expanded
"""


class Student:
    """ Class for Student """

    def __init__(self, first_name, last_name, age):
        """ Initializer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary Rep / JSON """
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            returns = {}
            for p, r in self.__dict__.items():
                if p in attrs:
                    returns[p] = r
            return returns
        else
            return self.__dict__

    def reload_from_json(self, json):
        """ Changes the attributes """
        for p, r in json.items():
            self.__dict__[p] = r
