#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or (a_dictionary.values()) == 0:
        return None
    key = ""
    value = -100
    for i in a_dictionary.keys():
        if a_dictionary[i] > value:
            value = a_dictionary[i]
            key = i
    return key
