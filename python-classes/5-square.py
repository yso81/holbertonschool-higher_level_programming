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
    
    def my_print(self):
        """
        prints in stdout the square with the character #
        if size is 0, prints an empty line.
        """
    
        if self.__size == 0:
            print()
        else: 
            for row in range(self.size):
                print("#" * self.__size)


if __name__ == "__main__":

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
