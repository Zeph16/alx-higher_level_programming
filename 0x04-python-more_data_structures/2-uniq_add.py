#!/usr/bin/python3


def uniq_add(my_list=[]):
    rec = []
    sum = 0
    for i in my_list:
        if i not in rec:
            sum += i
            rec.append(i)
    return sum
