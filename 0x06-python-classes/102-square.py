#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (float or int): The new size value.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator for squares based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparator for squares based on area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparator for squares based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal comparator for squares based on area."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparator for squares based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal comparator for squares based on area."""
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        """String representation of the Square instance."""
        return "Square({})".format(self.__size)

