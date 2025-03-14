"Apply any decorator to all methods of a class, with a decorator"

from types import FunctionType
from decoall_meta import tester
from decorators import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))    # Not __dict__
        return aClass
    return DecoDecorate

@decorateAll(tracer)                          # Use class deco, pass any func deco
class Person:                                 # Applies func decorator to methods
    def __init__(self, name, pay):            # Person = decorateAll(..)(Person)
        self.name = name                      # Person = DecoDecorate(Person)
        self.pay  = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

if __name__ == '__main__': tester(Person)

