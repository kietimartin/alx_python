'''
Alx task 0,Classes and Objecy project
'''

class Square:
    """
    This class holds a private square size attribute.
    It also checks if the value is an integer and is greater than zero and raises an execption
    """
    def __init__(self, size):
        # Private attribute
        self.__size = size

    def integer_checker(self):
        if self.__size.is_integer():
            return self.__size
        else:
            raise TypeError('size must be an integer')
        
    def greater_than_zero(self):
        if (self.__size >= 0):
            return self.__size
        else:
            raise ValueError('size must be >= 0')
        

        