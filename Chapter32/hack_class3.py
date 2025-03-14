class Hack:
    numInstances = 0
    def count(cls):                    # Per-class instance counters
        cls.numInstances += 1          # cls is lowest class above instance
    def __init__(self):
        self.count()                   # Passes self.__class__ to count
    count = classmethod(count)

class Sub(Hack):
    numInstances = 0
    def __init__(self):                # Redefines __init__ (to demo)
        Hack.__init__(self)

class Other(Hack):                     # Inherits __init__
    numInstances = 0

