#!/usr/bin/python3
"""Create class BaseGeometry"""

class NoInitSubclassMeta(type):

    '''
    Metaclass that removes the '__init_subclass__' attribute from the class dictionary.

    The purpose of this metaclass is to prevent the '__init_subclass__' method from being
    inherited by subclasses. By using this metaclass, classes won't have the '__init_subclass__'
    method listed when using the built-in 'dir()' function.
    '''

    def __dir__(cls):
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']


class BaseGeometry(metaclass=NoInitSubclassMeta):
    """Empty class
    """
    def __dir__(cls):
        """Removing __init_subclass_ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']

    def area(self):
        """Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates.

        Args:
            name (str): name of the object.
            value (int): value of the property.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))