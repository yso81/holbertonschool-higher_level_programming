#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/4-print_square.txt", verbose=True)
