#!/usr/bin/python3
"""
A module that contains a function that checks the type of obj
"""


def is_same_class(obj, a_class):
    """A function that compares the type of obj with a_class and returns
    True or False
    """
    return type(obj) == a_class
