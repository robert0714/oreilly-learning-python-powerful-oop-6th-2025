class Methods:
    def imeth(self, x):            # Instance method: passed a self
        print([self, x])           # Always expects a self instance

    def smeth(x):                  # Static method: no instance passed
        print([x])                 # Also a plain function from the class

    def cmeth(cls, x):             # Class method: gets class, not instance
        print([cls, x])            # Always expects a class, not instance

    smeth = staticmethod(smeth)    # Make smeth a static method (or use @: ahead)
    cmeth = classmethod(cmeth)     # Make cmeth a class method (or use @: ahead)

