#!/usr/bin/python3
def remove_char_at(str, n):
    removed = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        removed += str[i]
    return removed

