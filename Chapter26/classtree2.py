class C2: ...                    # Make superclass objects
class C3: ...

class C1(C2, C3):                # Make and link class C1
    def setname(self, who):      # Assign name: C1.setname
        self.name = who          # Self is either I1 or I2

I1 = C1()                        # Make two instances
I2 = C1()
I1.setname('sue')                # Sets I1.name to 'sue'
I2.setname('bob')                # Sets I2.name to 'bob'
print(I1.name)                   # Prints 'sue'

