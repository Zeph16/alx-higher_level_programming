#!/usr/bin/python3


def no_c(my_string):
    res = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        res += i
    return res
