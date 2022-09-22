#!/usr/bin/python3
""" Answer for Task 6 """


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    len= len(list_of_integers)
    m = int(len/ 2)
    li = list_of_integers

    if m - 1 < 0 and m + 1 >= len:
        return li[m]
    elif m - 1 < 0:
        return li[m] if li[m] > li[m + 1] else li[m + 1]
    elif m + 1 >= len:
        return li[m] if li[m] > li[m - 1] else li[m - 1]

    if li[m - 1] < li[m] > li[m + 1]:
        return li[m]

    if li[m + 1] > li[m - 1]:
        return find_peak(li[m:])
    return find_peak(li[:m])
