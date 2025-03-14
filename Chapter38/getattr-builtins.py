class GetAttr:
    cattr = 88                       # Attrs stored on class and instance
    def __init__(self):              # These skip getattr, but not getattribute
       self.iattr = 77

    def __len__(self):               # Redefine for len(): doesn't run getattr
        print('__len__: 66')
        return 66

    def __getattr__(self, attr):     # Provide __str__ if asked, else dummy func
        print('getattr:', attr)      # Never run for __str__: inherited from object
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute:
    cattr = 88                       # Similar, but catch all attributes
    def __init__(self):              # Except implicit fetches for built-in ops
        self.iattr = 77               

    def __len__(self):               # Redefine for len(): doesn't run getattribute
        print('__len__: 66')         # But explicit fetches of inherited __str__ do
        return 66

    def __getattribute__(self, attr):
        print('getattribute:', attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()

    # Defined attributes trigger getattribute but not getattr

    X.cattr                   # Class attr    (defined – skips getattr)
    X.iattr                   # Instance attr (defined – skips getattr
    X.other                   # Missing attr
    len(X)                    # __len__ defined explicitly: moot

    # Built-in ops do not invoke either getattr or getattribute
    # No defaults are inherited for these from object superclass

    try:    X[0]              # Tries to invoke __getitem__
    except: print('fail []')
    try:    X + 99            # Ditto, __add__
    except: print('fail +')
    try:    X()               # Ditto, __call__
    except: print('fail ()')

    # But explicit calls invoke both catchers

    X.__getitem__(0)
    X.__add__(99)
    X.__call__()

    # The implied object superclass defines a __str__ that precludes getattr
    # But the absolute getattribute is not called for implicit fetches either
 
    print(X.__str__())        # __str__: explicit call => only __getattr__ skipped
    print(X)                  # __str__: implicit via built-in => both skipped

