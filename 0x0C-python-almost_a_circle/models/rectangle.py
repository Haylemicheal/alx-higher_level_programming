#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set width value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set height value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def display(self):
        """Dispaly the rectangle"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(self.__x * " " + "#" * self.__width)

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args and len(args) != 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.width = arg
                elif c == 2:
                    self.height = arg
                elif c == 3:
                    self.x = arg
                elif c == 4:
                    self.y = arg
                c += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
