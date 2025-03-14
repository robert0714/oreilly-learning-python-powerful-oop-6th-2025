"Extend a class with a decorator"

def triple(obj):
    return obj.value * 3

def concat(obj):
    return obj.value + 'Code!'

def extender(aClass):
    aClass.triple = triple                   # Manages class, not instance
    aClass.concat = concat                   # Same as metaclass __call__
    return aClass

@extender
class Client1:                               # Client1 = Extender(Client1)
    def __init__(self, value):               # Rebound at end of class stmt
        self.value = value
    def double(self):
        return self.value * 2

@extender
class Client2:
    value = 'grok'

X = Client1('hack')                                       
print(X.double(), X.triple(), X.concat(), sep='\n')

Y = Client2()                                             
print(Y.triple(), Y.concat(), sep='\n')

