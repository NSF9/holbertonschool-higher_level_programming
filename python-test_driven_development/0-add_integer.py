#!/usr/bin/python3
"""
This module defines the add_integer function that adds two numbers.
It ensures both inputs are integers or floats (cast to int), and raises
TypeError or OverflowError where appropriate.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: The sum of a and b after casting to integers.

    Raises:
        TypeError: If a or b are not int or float.
        OverflowError: If a or b are infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a == float('inf') or a == float('-inf'):
        raise OverflowError()

    if b == float('inf') or b == float('-inf'):
        raise OverflowError()

    return int(a) + int(b)
