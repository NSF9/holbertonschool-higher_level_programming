#!/usr/bin/python3
"""
This module defines the CountedIterator class, which wraps an iterable and
counts how many items have been iterated over.
"""


class CountedIterator:
    """
    Iterator that counts the number of elements retrieved from an iterable.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator with an iterable object.

        Args:
            iterable: Any iterable object (list, tuple, etc.).
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next element from the iterator and increment the counter.
        """
        try:
            element = next(self.iterator)
            self.counter += 1
            return element
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Return the number of elements that have been iterated over.
        """
        return self.counter
