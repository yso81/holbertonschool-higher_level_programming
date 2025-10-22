#!/usr/bin/python3
"""
A class named BaseGeometry with an unimplemented area method
"""


class BaseGeometry:
    """
    Includes an area method that raises an Exception if not implemented by a subclass
    """

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")
