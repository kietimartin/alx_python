'''
This is task 3 in alx into to software engineering
This code gets a private class from a class and updates its value
'''
class Square:
    """
    This class holds a private square size attribute.
    It also checks if the value is an integer and is greater than zero and raises an exception.
    """
    def __init__(self, size=0):
        """
        Initialize the Square object with a size (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets a value to the private instance 'size'.
        Checks if the size is a non-negative integer.
        """
        self.validate_size(value)
        self.__size = value

    def validate_size(self, value):
        """
        Validate the size value separately for being an integer and being greater than zero.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
        Computes the area of the square given the size.
        """
        return self.__size * self.__size