#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square.
            Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.

        Args:
            value (tuple): The new position value as a tuple (x, y).

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters
        with the specified position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
