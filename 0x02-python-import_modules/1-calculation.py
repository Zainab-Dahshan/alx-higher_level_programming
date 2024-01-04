#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    x = 10
    y = 5
    print("{} + {} = {}".format(x, y, add(x, y)))
    print("{} - {} = {}".format(a, b, sub(x, y)))
    print("{} * {} = {}".format(a, b, mul(x, y)))
    print("{} / {} = {}".format(a, b, div(x, y)))
