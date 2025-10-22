#!/usr/bin/python3
"""
Checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj's class is a subclass of a_class, and obj's class
        is not exactly a_class itself; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
