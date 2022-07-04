#!/usr/bin/python3
"""
A module that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list and contains a method
    print sorted list
    """
    def print_sorted(self):
        """
        Print sorted list
        """
        print(sorted(self[:]))
