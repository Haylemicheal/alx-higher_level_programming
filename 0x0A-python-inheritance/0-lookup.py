#!/usr/bin/python3
"""
A module that contains a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    A function that returns available attributes of an obj
    """
    return dir(obj)
