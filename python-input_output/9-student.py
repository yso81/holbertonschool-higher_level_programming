#!/usr/bin/python3
"""
    Provides a method to retrieve a dictionary representation of the instance
    for JSON serialization
"""


class Student:
    """
    Defines a student with first name, last name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        Only attributes with simple data structures (list, dictionary, string,
        integer, boolean) are included, mirroring the behavior of
        class_to_json.py

        Returns:
            dict: A dictionary containing the serializable attributes of the
            Student instance
        """
        json_dict = {}
        for attr_name in dir(self):
            is_special_attr = attr_name.startswith('__')
            is_callable = callable(getattr(self, attr_name))
            if not is_special_attr and not is_callable:
                attr_value = getattr(self, attr_name)

                if isinstance(attr_value,
                              (list, dict, str, int, bool)):
                    json_dict[attr_name] = attr_value
        return json_dict
