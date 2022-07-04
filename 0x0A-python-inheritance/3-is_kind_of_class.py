#!/usr/bin/python3
"""
3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns true if the obj is an instance of a class
    that inherited from, the specified class
    """
    return isinstance(obj, a_class)
