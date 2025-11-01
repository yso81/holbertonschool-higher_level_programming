#!/usr/bin/python3
"""
basic serialization module that adds the functionality to serialize a Python
dictionary to a JSON file and deserialize the JSON file to recreate the Python
Dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file

    Args:
        data (dict): The Python dictionary to serialize
        filename (str): The filename of the output JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: The deserialized Python dictionary
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
