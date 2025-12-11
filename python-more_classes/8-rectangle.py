#!/usr/bin/python3
"""
Module: rectangle
Defines a Rectangle class with width, height,
area calculation, perimeter, comparison, and string representation.
"""


class Rectangle:
    """
    Represents a rectangle defined by width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string of the rectangle using `print_symbol`.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                         for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation that can recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when instance is deleted. Decrements counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area.
                      If equal, returns rect_1.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
