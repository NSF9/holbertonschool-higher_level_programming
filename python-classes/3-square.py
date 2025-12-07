#!/usr/bin/python3
"""
This module defines a Square class that allows creating square objects
with a private size attribute and provides a method to calculate area.
"""


class Square:
    '''
    Represents a square with a given size.

    Attributes:
        __size (int): The length of the square's side (private).

    Methods:
        area(): Returns the area of the square.
    '''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
