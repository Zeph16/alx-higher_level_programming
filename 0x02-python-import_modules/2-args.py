#!/usr/bin/python3
import sys


def main():
    list = sys.argv
    if (len(sys.argv) == 1):
        print("0 arguments.")
        return
    elif (len(list) == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(list) - 1))
    for i in range(1, len(list)):
        print("{:d}: {}".format(i, list[i]))


if __name__ == "__main__":
    main()
