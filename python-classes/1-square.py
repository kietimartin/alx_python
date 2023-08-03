'''
Alx task 0,Classes and Objecy project
'''

class Square:
    """
    This class holds a private square size attribute.
    It also checks if the value is an integer and is greater than zero and raises an execption
    """
    def __init__(self, size=0):
        # Private attribute
        pass
        # self.__size = size

    def integer_checker(self):
        if self.__size.is_integer():
            self.__size = size
            
        else:
            raise TypeError('size must be an integer')
        
    def greater_than_zero(self):
        if (self.__size >= 0):
            self.__size = size
        else:
            raise ValueError('size must be >= 0')
        