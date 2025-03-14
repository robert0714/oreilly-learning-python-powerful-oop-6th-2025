class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here.  Displays instance attrs only; self is
    instance of lowest class; __X naming avoids clashing with client's attrs.
    Works for classes with slots: a __dict__ is ensured by lack of slots here.
    """
    def __attrnames(self):
        result = '\n'
        for attr in sorted(self.__dict__):                      # Slots okay
            result += f'\t{attr}={self.__dict__[attr]!r}\n'     # Repr for quotes
        return result

    def __str__(self):
        return (f'<Instance of {self.__class__.__name__}, '     # My class's name
                f'address {id(self):#x}:'                       # My address (hex)
                f'{self.__attrnames()}>')                       # name=value list

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)      # Test class in this module

