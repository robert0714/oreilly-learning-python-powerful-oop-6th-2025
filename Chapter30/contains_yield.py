from contains import *

class ItersYield(Iters):
    def __iter__(self):                    # Preferred for iteration
        trace('@iter @next')               # Allows multiple active iterators
        for x in self.data:                # Implicit generator alternative
            yield x
            trace('@next')

if __name__ == '__main__': self_test(ItersYield)      # Test Iters here

