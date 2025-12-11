#!/usr/bin/python3
"""
Module: rectangle
Defines a Rectangle class with width, height,
area calculation, perimeter, and string representation.
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
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """this is how to print for the Rectangle class """
        if self.width <= 0 or self.height <= 0:
            return ""
        else:
            lines = []
            for i in range(self.height):
                lines.append(f"{str(self.print_symbol)}" * self.width)

        return "\n".join(lines)

    def __repr__(self):
        """
        Returns the official string representation of the rectangle
        that can be used to recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the bigger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            Rectangle: The rectangle with the larger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square (rectangle with equal sides).

        Args:
            size (int): Size of both width and height.

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
