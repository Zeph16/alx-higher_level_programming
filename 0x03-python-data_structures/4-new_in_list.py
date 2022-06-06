#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list) or len(my_list) == 0:
        return "None"
    templist = []
    for i in range(len(my_list)):
        if i == idx:
            templist.append(element)
            continue
        templist.append(my_list[i])
    return templist
