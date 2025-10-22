#!/usr/bin/python3
"""
A class named BaseGeometry with an unimplemented area method and an
integer validation method
"""


class BaseGeometry:
    """
    A base class for geometry-related operations
    Includes:
    area method that raises an Exception if not implemented by a subclass
    integer_validator method for validating integer values
    """

    def area(self):
        """
        Public instance method that raises an Exception
        This method is expected to be implemented by subclasses
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Public instance method that validates an integer value

        Args:
            name (str): The name of the value (assumed to be a string)
            value: The value to validate

        Raises:
            TypeError: If value is not an integer, with message "<name> must 
            be an integer"
            ValueError: If value is less than or equal to 0, with message
            "<name> must be greater than 0"
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
