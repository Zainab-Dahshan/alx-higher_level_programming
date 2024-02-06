#!/usr/bin/python3
""" my files """


def read_file(filename=""):
    """my func """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
