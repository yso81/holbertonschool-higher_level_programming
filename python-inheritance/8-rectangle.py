#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance

        Args:
            width (int): The width of the rectangle

            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    my_rect = Rectangle(10, 5)
    print(my_rect)
