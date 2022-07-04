#!/usr/bin/python3
"""
Task 1 - MyList Class that prints a list
"""


class MyList(list):
    """ Class that operates with lists """

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
