#!/usr/bin/python3
"""
4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    Returns true if the obj is an instance of a class that inherited
    directly or indirectly from a class otherwise return False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
