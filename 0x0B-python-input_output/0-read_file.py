#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """A function to read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
