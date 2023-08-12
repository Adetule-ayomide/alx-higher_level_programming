#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    args = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    signs = argv[2]
    b = int(argv[3])
    if signs not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if signs == "+":
            result = add(a, b)
        elif signs == "-":
            result = sub(a, b)
        elif signs == "*":
            result = mul(a, b)
        elif signs == "/":
            result = div(a, b)
        print("{} {} {} = {}".format(a, signs, b, result))


if __name__ == "__main__":
    main()
