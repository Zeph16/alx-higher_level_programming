#!/usr/bin/python3
"""
Task 10 - Student JSON expanded
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
