#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list) or len(my_list) == 0:
        return "None"
    templist = my_list.copy()
    templist[idx] = element
    return templist
