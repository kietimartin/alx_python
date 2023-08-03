"""
This is task 1 of the inheritance project
"""
def is_same_class(obj, a_class):
    """
    This returns true if the object is exactly an instance of the specified class otherwise false
    """
    return type(obj) is a_class