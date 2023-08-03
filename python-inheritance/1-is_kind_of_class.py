'''
This is task 2 of the inheritance project
'''
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or an instance of a class inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
