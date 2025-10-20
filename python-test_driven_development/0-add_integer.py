#!/usr/bin/python3
"""
Function to add two integers and its doctest runner.
"""


def add_integer(a, b=98):
    """My addition function

    Args:
        a: first integer (int or float)
        b: second integer (int or float, defaults to 98)
    
    Raises:
        TypeError: If a or b is not an integer or float

    Returns:
        The return value. a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt", verbose=True)
