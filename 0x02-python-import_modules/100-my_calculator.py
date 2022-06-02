#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    input = sys.argv
    if len(input) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if input[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(input[1])
    op = input[2]
    b = int(input[3])
    print("{} {} {} = ".format(a, op, b), end='')
    if op ==  "+":
        print(add(a, b))
    elif op ==  "-":
        print(sub(a, b))
    elif op ==  "*":
        print(mul(a, b))
    elif op ==  "/":
        print(div(a, b))
        

if __name__ == "__main__":
    main()
