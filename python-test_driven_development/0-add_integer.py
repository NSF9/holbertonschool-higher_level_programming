#!/usr/bin/python3
def add_integer(a, b=98):

    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integers")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integers")
    if a == float("inf") or a == float("-inf"):
        raise OverflowError
    if b == float("inf") or b == float("-inf"):
        raise OverflowError
    return int(a + b)
