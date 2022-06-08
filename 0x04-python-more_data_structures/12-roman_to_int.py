#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    string_list = list(roman_string)
    delayed = string_list.copy()
    delayed.append('I')
    string_list.reverse()
    delayed.reverse()
    converted = 0
    for i in range(len(string_list)):
        value = roman[string_list[i]]
        if (value > converted or value == prev):
            converted += value
        else:
            converted -= value
        prev = value
    return converted
