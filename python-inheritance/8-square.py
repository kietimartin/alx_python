#!/usr/bin/python3
"""
Creates a Square class.
"""


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    Private instance attribute 'size'.
    Public method 'area()'.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square.
        Args:
            - size: size of the square
        """

        # Validate the 'size' argument using the inherited method
        self.integer_validator("size", size)

        # Initialize the base class (Rectangle) using the provided 'size' argument twice
        # This assumes that the base class 'Rectangle' accepts two arguments for width and height
        super().__init__(size, size)

        # Store the 'size' attribute
        self.__size = size

    def area(self):
        """
        Computes the area of a Square instance.
        Overrides the area() method from Rectangle.
        """

        return self.__size ** 2