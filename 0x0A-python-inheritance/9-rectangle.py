#!/usr/bin/python3
"""9-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """A constractor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Representation of the obj"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
