class ListInherited:
    """
    Use dir() to collect both instance attrs and names inherited from
    its classes.  This includes default names inherited from the implied 
    'object' superclass above topmost classes.  getattr() can fetch 
    inherited names not in self.__dict__.  

    Caution: use __str__, not __repr__, or else this loops when printing 
    bound methods that may be returned for some attributes by getattr().
    This will normally fail for class "slots" attributes not yet assigned.
    """

    def __attrnames(self, unders=False):
        result = '\n'
        for attr in dir(self):                                   # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':           # Built-in names
                result += f'\t{attr}\n' if unders else ''        # Skip built-ins?
            else:
                result += f'\t{attr}={getattr(self, attr)!r}\n'
        return result

    def __str__(self):
        return (f'<Instance of {self.__class__.__name__}, '      # My class's name
                f'address {id(self):#x}:'                        # My address (hex)
                f'{self.__attrnames()}>')                        # name=value list

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)      # Test class in this module

