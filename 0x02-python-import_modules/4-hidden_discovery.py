#!/usr/bin/python3

def main():
    list = dir("hidden_4.pyc")
    for i in range(0, len(list)):
        if list[i][0] != '_':
            print("{}".format(list[i]))


if __name__ == "__main__":
    main()
