#!/usr/bin/python3
"""
Appends a string to a text file (UTF8) and returns the number of characters
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number of characters

    Args:
        filename (str): The name of the file to append to
        text (str): The string to append to the file

    Returns:
        int: The number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
