'''
Alx task 0,Classes and Objecy project
'''

class Square:
    """
    This class holds a private square size attribute.
    It also checks if the value is an integer and is greater than zero and raises an execption
    """
    def __init__(self, size=0):
        """
        Initialize the Square object with a size (default is 0).
        """
        self.__size = self.integer_checker(size)
        self.greater_than_zero()

    def get_size(self):
        """
        Get the size of the square.
        """
        return self.__size
    
    def set_size(self, size):
        """
        Set the size of the square after checking if the value is a positive integer.
        """
        self.__size = self.integer_checker(size)
        self.greater_than_zero()

    def integer_checker(self, value):
        """
        Check if the given value is an integer. If not, raise a TypeError.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        return value
        
    def greater_than_zero(self):
        """
        Check if the size is greater than or equal to 0. If not, raise a ValueError.
        """
        if self.__size < 0:
            raise ValueError('size must be >= 0')
    
    def area(self):
        """
        Computes the area of the square given the size
        """
        area = self.__size * self.__size

        return area