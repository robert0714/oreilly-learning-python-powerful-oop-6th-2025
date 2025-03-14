class C2: ...                    # Make superclass objects
class C3: ...

class C1(C2, C3):
    def __init__(self, who):     # Set name when constructed
        self.name = who          # Self is either I1 or I2

I1 = C1('sue')                   # Sets I1.name to 'sue'
I2 = C1('bob')                   # Sets I2.name to 'bob'
print(I1.name)                   # Prints 'sue'

