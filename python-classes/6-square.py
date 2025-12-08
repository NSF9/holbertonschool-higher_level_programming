#!/usr/bin/python3
"""
This module defines a Square class with property-based
size control, area calculation, and a custom print method.
"""


class Square:
    """
    Represents a square with a validated size and position.

    Attributes:
        __size (int): The length of a side of the square (private).
                __position (tuple):
            Tuple with 2 positive integers representing position.
    """

    def __init__(self, size=0,
                 postion=(0, 0)):
        """
        Initializes the square with an optional size and position.

        Args:
            size (int): The size of the square's side (default is 0).
            postion (tuple): The position offset of the square
                             (default is (0, 0)).
        """
        self.size = size
        self.position = postion

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): New value for the size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in range(len(value)):
                if (not isinstance(value[i], int) or value[i] < 0 or
                        len(value) != 2):
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters, considering the position.
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] != 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.__position[0] != 0:
                    print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
