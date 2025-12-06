#!/usr/bin/python3
"""
Module that defines a function to find the maximum integer in a list.
"""


def max_integer(numbers=[]):
    """
    Returns the maximum integer in a list of integers.
    
    Args:
        numbers (list): List of integers.

    Returns:
        int: The maximum integer in the list.
        None: If the list is empty.
    """
    if len(numbers) == 0:
        return None

    result = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > result:
            result = numbers[i]
        i += 1

    return result
