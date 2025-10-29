#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to be serialized and written to the file
        filename (str): The name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename (str): The path to the JSON file

    Returns:
        object: The Python object represented by the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

filename = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

save_to_json_file(my_list, filename)
