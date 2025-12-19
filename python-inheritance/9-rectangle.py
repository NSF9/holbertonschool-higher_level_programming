#!/usr/bin/python3
"""
Module that defines a Rectangle class inheriting from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates width and height as positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a user-friendly string representation of the rectangle.

        Returns:
            str: Formatted string like [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns an official string representation of the rectangle.
        Used mainly for debugging.
        """
        return self.__str__()
