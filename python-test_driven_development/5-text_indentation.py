#!/usr/bin/python3
"""
This module defines the function text_indentation
which prints a text with 2 new lines after each
of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    buffer = ""

    for char in text:
        buffer += char
        if char in special_chars:
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())
