"""
Generic lister-mixin tester: similar to transitive reloader in
Chapter 25, but passes a class object to tester (not function),
and testByNames adds loading of both module and class by name
strings here, in keeping with Chapter 31's factories pattern.
"""
import importlib

def tester(listerclass, sept=False):    
    "Pass any lister class to listerclass"

    class Super:
        def __init__(self):                 # Superclass __init__
            self.data1 = 'code'             # Create instance attrs
        def method1(self):
            pass

    class Sub(Super, listerclass):          # Mix in method1 and a __str__
        def __init__(self):                 # Listers have access to self
            Super.__init__(self)            # Or super().__init__()
            self.data2 = 'Python'           # More instance attrs
            self.data3 = 3.12
        def method2(self):                  # Define another method here
            pass

    instance = Sub()                        # Build instance with lister's __str__
    print(instance)                         # Run mixed-in __str__ (or via str(x))
    if sept: print(f'\n{'-' * 80}\n')

def testByNames(modname, classname, sept=False):
    modobject   = importlib.import_module(modname)    # Import mod by namestring
    listerclass = getattr(modobject, classname)       # Fetch attr by namestring
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance',  'ListInstance',  True)      # Test all three here
    testByNames('listinherited', 'ListInherited', True)      # See others ahead...
    testByNames('listtree',      'ListTree',      False)

