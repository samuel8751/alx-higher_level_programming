#!/usr/bin/python3
"""
Module: 10-square

Defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class: Square

    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(): Calculates the area of the square.

    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call the constructor of the parent class (Rectangle)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representation of the Square.

        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

# Example usage
if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

