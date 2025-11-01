#!/usr/bin/python3
"""
serialize and deserialize custom Python objects using the pickle module
"""
import pickle
import os


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object to a file using pickle

        Args:
            filename (str): The filename to save the serialized object to

        Returns:
            bool: True if serialization was successful, False otherwise
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception as e:
            print(f"Error during serialization: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance of CustomObject from a file using pickle

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject or None: An instance of CustomObject if successful, None otherwise
        """
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return None
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            else:
                print(f"Error: Data in '{filename}' is not a CustomObject instance.")
                return None
        except (pickle.UnpicklingError, EOFError) as e:
            print(f"Error during deserialization (malformed file): {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during deserialization: {e}")
            return None


if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
