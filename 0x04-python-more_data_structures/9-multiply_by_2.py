#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}
    if a_dictionary:
        for i in a_dictionary.keys():
            new.update({i: a_dictionary[i] * 2})
    return new
