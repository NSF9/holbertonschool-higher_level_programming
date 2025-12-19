#!/usr/bin/python3
"""
Module that defines a Square class inheriting from Rectangle.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Ensures that size is a positive integer and both width and height are equal.
    """

    def __init__(self, size):
        """
        Initializes a Square with the given size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: Formatted string like [Square] size/size
        """
        return f"[Square] {self.__size}/{self.__size}"
