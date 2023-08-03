'''
Alx,Classes and Object project
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
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        '''
        Sets a value to the private instance 'size'
        checks if the size is an integer
        chacks if the size is greater than 0
        '''
        if value.is_integer():
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Computes the area of the square given the size
        """
        area = self.__size * self.__size

        return area