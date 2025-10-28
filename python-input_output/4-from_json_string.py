#!/usr/bin/python3
"""
Returns an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): The JSON string to be deserialized to a Python object

    Returns:
        obj: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)
