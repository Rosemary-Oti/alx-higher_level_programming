#!/usr/bin/python3

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

