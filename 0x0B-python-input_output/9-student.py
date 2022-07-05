#!/usr/bin/python3
"""
Task 9 - Student
"""


class Student:
    """ Class for Student """

    def __init__(self, first_name, last_name, age):
        """ Initializer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Dictionary Rep / JSON """
        return self.__dict__
