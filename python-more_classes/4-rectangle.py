#!/usr/bin/python3
"""
This module creates an empty class Rectangle
"""


class Rectangle:
    """
    an empty class that defines a rectangle.

    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Args:
        width
        height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        raise:
        Type error: if size is not an integer
        Value error: if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        raise:
        Type error: if size is not an integer
        Value error: if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle using the "#"
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for row in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Returns a string representation that can recreate the object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
