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

        self.__width = width
        self.__height = height

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
