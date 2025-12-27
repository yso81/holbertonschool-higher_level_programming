#!/usr/bin/python3
import abc
import math


class Shape(abc.ABC):
    """
    Abstract that defines a shape
    """

    @abc.abstractmethod
    def area(self):
        """
        Abstract that defines the area of a shape
        """
        pass

    @abc.abstractmethod
    def perimeter(self):
        """
        Abstract that defines the perimeter of a shape
        """
        pass


class Circle(Shape):
    """
    Implementing the Circle subclass with area and perimeter method
    """
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Error! Must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return math.pi * self.radius * 2


class Rectangle(Shape):
    """
    Implementing the Rectangle subclass with area and perimeter method
    """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Accepts any object with the area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    from task_01_duck_typing import Circle, Rectangle, shape_info

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
