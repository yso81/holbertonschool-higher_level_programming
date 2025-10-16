#!/usr/bin/python3
"""
This module creates a Square class.
"""


class Square:
    """
    Defines a square class with Private instance attribute: Size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a New square instance.

        Args :
        Size : The size of the square.
        position (tuple): the position of the square (x,y)

        """

        self.__size = size
        self.__position = position

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

    def position(self):
        """
        retrieves the position of the sqaure.

        returns the tuple(x, y) of the square position.
        """

        return self.__position

    def position(self, value):
        """
        sets the position of the square.

        Args:
        Value (tuple):  new position ofthe square (x, y)

        Raises:
        TypeError: If value is not a tuple having 2 integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
           raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the current square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        if size is 0, prints an empty line.

        Handles size 0 and position of square.
        """

        if self.__size == 0:
            print()

        for row in range(self.__position[1]):
            print("")

        for row in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
