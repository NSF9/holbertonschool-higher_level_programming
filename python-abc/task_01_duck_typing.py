#!/usr/bin/python3
"""
This module defines an abstract Shape class and its Circle and Rectangle subclasses.
It also includes a utility function to display area and perimeter info for a shape.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape that implements area and perimeter calculations.
    """

    pi = 3.141592653589793

    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        Radius is always stored as an absolute value.
        """
        super().__init__()
        self.__radius = abs(radius)

    def area(self):
        """
        Return the area of the circle.
        """
        return (self.__radius ** 2) * self.pi

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * self.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle shape that implements area and perimeter calculations.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.
        """
        super().__init__()
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape object.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
