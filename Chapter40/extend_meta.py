"Extend a class with a metaclass"

def triple(obj):
    return obj.value * 3                                  # Functions to insert
                                                          # Methods if in a class
def concat(obj):                                          # Where "obj" is "self"
    return obj.value + 'Code!'

class Extender(type):
    def __new__(meta, classname, supers, classdict):      # On client-class creation
        classdict['triple'] = triple                      # Add funcs as attributes 
        classdict['concat'] = concat
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):                            # Created from Extender
        self.value = value                                # Own + inserted methods
    def double(self):
        return self.value * 2

class Client2(metaclass=Extender):                        # Created from Extender
    value = 'grok'                                        # Inherited class data

X = Client1('hack')                                       
print(X.double(), X.triple(), X.concat(), sep='\n')

Y = Client2()                                             
print(Y.triple(), Y.concat(), sep='\n')

