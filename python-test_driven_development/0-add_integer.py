#!/usr/bin/python3
#!/usr/bin/python3
"""
This module defines the add_integer function that adds two numbers.
It ensures both inputs are integers or floats (cast to int), and raises
TypeError or OverflowError where appropriate.
"""

def add_integer(a, b=98):

    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float("inf") or a == float("-inf"):
        raise OverflowError
    if b == float("inf") or b == float("-inf"):
        raise OverflowError
    return int(a + b)
