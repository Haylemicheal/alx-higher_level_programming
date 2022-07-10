#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""
test_rectangle
import the unittest module, Base class and the Rectangle class
"""


class TestRectangle(unittest.TestCase):
    """A test class for Rectangle"""
    def test_id(self):
        """Test the id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, 12)

    def test_height(self):
        """Test the height"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.height, 2)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_height(self):
        """Test the height"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        r1.width = 11
        self.assertEqual(r1.width, 11)

    def test_x(self):
        """Test the x value"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.x, 0)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_y(self):
        """Test the y value"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.y, 0)
        r1.y = 10
        self.assertEqual(r1.y, 10)

    def test_type_and_value(self):
        """Test the type of the attributes"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            r1.width = "A"
        with self.assertRaises(ValueError):
            r1.width = -2
        with self.assertRaises(TypeError):
            r1.height = "A"
        with self.assertRaises(ValueError):
            r1.height = -2
        with self.assertRaises(TypeError):
            r1.y = "A"
        with self.assertRaises(ValueError):
            r1.y = -2
        with self.assertRaises(TypeError):
            r1.x = "A"
        with self.assertRaises(ValueError):
            r1.x = -2

    def test_area(self):
        """Test the area"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
