#!/usr/bin/python3
def uppercase(str):
    for c in str:
        switch = 0
        if ord(c) < 123 and ord(c) > 96:
            switch = 32
        print("{:c}".format(ord(c) - switch), end='')
    print()
