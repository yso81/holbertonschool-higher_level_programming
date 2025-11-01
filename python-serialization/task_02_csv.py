#!/usr/bin/python3
"""
a function named convert_csv_to_json that takes the CSV filename as its
parameter and writes the JSON data to data.json
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to JSON format and writes it to data.json

    Args:
        csv_filename (str): The name of the CSV file to convert

    Returns:
        bool: True if the conversion was successful or else False
    """
    data = []
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")