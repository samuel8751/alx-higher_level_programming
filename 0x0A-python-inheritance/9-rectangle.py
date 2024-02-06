#!/usr/bin/python3
"""
Module: 9-rectangle

Defines the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class: Rectangle

    Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        area(): Calculates the area of the rectangle.

    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A string representation of the Rectangle.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# Example usage
if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())

