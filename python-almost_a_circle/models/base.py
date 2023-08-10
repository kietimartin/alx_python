'''
This is the almost a circle project in  the alx intro to swe
'''
class Base:
    '''
    This is the base class containing a private class attribute
    and other functions

    attributes:
        id(int)
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        This is the initialization function - creates instances of base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

