#!/usr/bin/python3
"""
Checks if an object is an instance of, or if the object is an instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class (or a tuple of classes) to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass thereof;
        otherwise, False.
    """
    return isinstance(obj, a_class)
