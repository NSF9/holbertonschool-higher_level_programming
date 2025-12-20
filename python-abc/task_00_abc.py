#!/usr/bin/python3
"""
This module defines an abstract Animal class and its concrete subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by all subclasses to return
        the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound that a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound that a cat makes.
        """
        return "Meow"
