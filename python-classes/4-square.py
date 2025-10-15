#!/usr/bin/python3
"""
This module creates a Square class.
"""

class Square:
    """
    Defines a square class with Private instance attribute: Size
    """
    
    def __init__(self, size=0):
        """
        Initialises a New square instance.

        Args: Size

        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square.

        Raise:
        Type error: if size is not an integer
        Value error: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the current square.
        """
        return self.__size ** 2


if __name__ == "__main__":

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
