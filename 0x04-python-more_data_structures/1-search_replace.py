#!/usr/bin/python3


def search_replace(my_list,search,replace):
    removed = []
    for i in my_list:
        if i == search:
            removed.append(replace)
            continue
        removed.append(i)
    return removed
