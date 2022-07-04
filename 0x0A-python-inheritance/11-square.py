#!/usr/bin/python3
"""11-square.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """A constractor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of square"""
        return self.__size ** 2

    def __str__(self):
        """Representation of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
