#!/usr/bin/python3
"""
6-max_integer module
"""

def max_integer(list=[]):
    """
    Finds the max integer in a list of integers.
    If the list is empty, returns None.
    """
    if not list:
        return None
    
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value
