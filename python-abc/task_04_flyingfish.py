#!/usr/bin/python3
"""
This module defines a multiple inheritance example using Fish, Bird,
and FlyingFish classes to demonstrate abstract behavior and shared methods.
"""

from abc import ABC, abstractmethod


class Fish(ABC):
    """
    Abstract base class representing a Fish.
    """

    @abstractmethod
    def swim(self):
        """
        Abstract method that should define how the fish swims.
        """
        pass

    @abstractmethod
    def habitat(self):
        """
        Abstract method that should define the habitat of the fish.
        """
        pass


class Bird(ABC):
    """
    Abstract base class representing a Bird.
    """

    @abstractmethod
    def fly(self):
        """
        Abstract method that should define how the bird flies.
        """
        pass

    @abstractmethod
    def habitat(self):
        """
        Abstract method that should define the habitat of the bird.
        """
        pass


class FlyingFish(Fish, Bird):
    """
    A FlyingFish class that inherits from both Fish and Bird,
    and implements all abstract methods.
    """

    def fly(self):
        """
        Implementation of flying behavior for flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Implementation of swimming behavior for flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Defines the unique habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
