'''
This is task 3 of alx inheritance project
'''
class BaseGeometry:
    """BaseGeometry class"""

    def __dir__(self):
        """Override default behavior of the dir() method."""
        attributes = super().__dir__()
        list_to_return = []
        for attr in attributes:
            if attr != "__init_subclass__":
                list_to_return.append(attr)
        return list_to_return
