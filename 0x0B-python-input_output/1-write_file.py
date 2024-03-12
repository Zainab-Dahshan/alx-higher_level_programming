#!/usr/bin/python3
""" my len function  """


def write_file(filename="", text=""):
    """ length of function """
    with open(filename, 'w', encoding="utf-8") as ff:
        rr = ff.write(text)
    return rr
