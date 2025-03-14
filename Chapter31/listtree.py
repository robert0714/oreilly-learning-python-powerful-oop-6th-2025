class ListTree:
    """
    Mix-in that returns a __str__ trace of the entire class tree and all
    its objects' attrs at and above the self instance.  The display is 
    run by print() automatically; use str() to fetch as a string.  This:

    -Uses __X pseudoprivate attr names to avoid conflicts with clients
    -Recurses to superclasses explicitly in DLFR (though not MRO) order
    -Uses __dict__ instead of dir() because attrs are listed per object
    -Supports classes with slots: lack of slots here ensures a __dict__
    """

    def __attrnames(self, obj, indent, unders=True):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                if unders: result += f'{spaces}{attr}\n'
            else:
                result += f'{spaces}{attr}={getattr(obj, attr)!r}\n'
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        preamble = (f'\n{dots}'
                    f'<Class {aClass.__name__}'
                    f', address {id(aClass):#x}')

        if aClass in self.__visited:
            return preamble + ': (see above)>\n'                # Already listed
        elif aClass is object:
            self.__visited[aClass] = True
            return preamble + ': (see dir(object))>\n'          # Skip object's 24
        else:
            self.__visited[aClass] = True
            here  = self.__attrnames(aClass, indent)            # My attrs + supers
            above = ''
            for Super in aClass.__bases__:
                above += self.__listclass(Super, indent + 4)
            return preamble + f':\n{here}{above}{dots}>\n'

    def __str__(self):
        self.__visited = {}
        here  = self.__attrnames(self, 0)                       # My attrs
        above = self.__listclass(self.__class__, 4)             # My supers tree
        return (f'<Instance of {self.__class__.__name__}'       # My class's name
                f', address {id(self):#x}'                      # My address (hex)
                f':\n{here}{above}>')                           # attrs + supers

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)      # Test class in this module

