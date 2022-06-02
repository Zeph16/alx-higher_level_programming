#!/usr/bin/python3
import hidden_4


def main():
    list = dir(hidden_4)
    for i in list:
        if i.startswith("__"):
            continue
        print("{}".format(i))


if __name__ == "__main__":
    main()
