#!/usr/bin/python3
"""
Task 12 - My Int
"""


class MyInt(int):
    """ Inverted == and != operations """

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
