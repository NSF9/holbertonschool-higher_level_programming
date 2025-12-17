#!/usr/bin/python3
"""
This module defines the MyList class which extends the built-in list class
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of list that adds a method to print
    the list elements sorted in ascending order.
    """

    def __init__(self, *args):
        """
        Initialize the list with optional elements.
        """
        super().__init__(args)

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order,
        without modifying the original list.
        """
        print(sorted(self))
