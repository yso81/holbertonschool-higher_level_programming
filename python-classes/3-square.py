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

        Raise:
        Type error: if size is not an integer
        Value error: if size is less than 0.
        """
    
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the current square.
        """
    
        self.area = self.__size **2
        return self.area


if __name__ == "__main__":

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
