#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a new Square instance

        Args:
            size (int): The size (width and height) of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
