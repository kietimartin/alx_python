'''
This is task 4 in alx-python into to software engineering
This code prints out a square made of hashes
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
    
    def my_print(self, rows=0,col=0):
        '''
        This is a method that created a square made of hashes
        '''
        self.row = rows
        self.col = col 

        if rows >= self.__size:
            if (col > 0) or (col <= self.__size):
                a = '#'
                print(a, end='')
                col += 1
            elif col == self.size:
                print(a)

        elif (rows == 0):
            print('')