#!/usr/bin/python3


import math


class MagicClass:
    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius (int or float, optional):
            The radius of the circle (default is 0).

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = float(radius)

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
