'''
This is task 5
'''
class NoInitSubclassMeta(type):
    """
    A metaclass that removes the '__init_subclass__' attribute from class directory.
    """
    def __dir__(cls):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']


class BaseGeometry(metaclass=NoInitSubclassMeta):
    """
    BaseGeometry class defining a common interface for geometric operations.
    """
    def __dir__(cls):
        """
        Remove '__init_subclass__' attribute from the class directory.
        """
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: if 'area' is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")
