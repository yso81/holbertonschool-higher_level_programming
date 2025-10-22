#!/usr/bin/python3
"""
    A class MyList that inherits from list
"""


class MyList(list):
    """
    Provides a method to print the list elements in ascending order
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order
        """
        print(sorted(self))
