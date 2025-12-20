#!/usr/bin/python3
"""
This module defines mixin classes for swim and fly behavior,
and a Dragon class that can swim, fly, and roar.
"""


class SwimMixin:
    """
    Mixin class that provides swimming ability.
    """

    def swim(self):
        """
        Print a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability.
    """

    def fly(self):
        """
        Print a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can swim, fly, and roar.
    Inherits behavior from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
