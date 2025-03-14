class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def smeth(x):                  # Static: no instance passed
        print([x])

    @classmethod
    def cmeth(cls, x):             # Class: gets class, not instance
        print([cls, x])

    @property                      # Property: computed on fetch
    def name(self):
        return 'Pat ' + self.__class__.__name__

