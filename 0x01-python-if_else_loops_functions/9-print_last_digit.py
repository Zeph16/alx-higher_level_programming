#!/usr/bin/python3
def print_last_digit(number):
    number = number * -1 ? number < 0 : number
    print(f"{number % 10}")
    return number % 10
