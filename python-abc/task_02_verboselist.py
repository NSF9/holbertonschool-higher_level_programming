#!/usr/bin/python3
"""
This module defines the VerboseList class which extends the built-in list class
to include print statements for tracking list operations.
"""


class VerboseList(list):
    """
    Subclass of list that prints messages on append, extend, remove, and pop.
    """

    def append(self, element):
        """
        Append an element to the list and print a message.
        """
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print the count.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item and print a message if found.
        """
        if item not in self:
            return
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last), and print the popped item.
        """
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
