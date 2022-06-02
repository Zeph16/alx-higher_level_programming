#!/usr/bin/python3
import sys


def main():
    list = sys.argv
    add = 0
    for i in range(1, len(list)):
        add += int(list[i])
    print("{:d}".format(add))


if __name__ == "__main__":
    main()
