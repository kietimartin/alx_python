'''
This is task 5
'''
class BaseGeometry:
    '''
    This code does:
        -Define Area function.
        -Validate an integer value
    '''
    def area(self):
        """
        Define Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): Name of the value being validated.
            value (int): Value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        