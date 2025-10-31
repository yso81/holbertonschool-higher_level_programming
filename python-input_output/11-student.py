#!/usr/bin/python3
"""
Defines a student with first name, last name, and age
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): A list of strings specifying
            which attributes to retrieve
            If None, all attributes are retrieved

        Returns:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        elif (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
        else:
            return self.__dict__
    
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))
