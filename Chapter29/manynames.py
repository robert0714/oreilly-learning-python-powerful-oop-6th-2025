X = 11                       # Global (module) X (manynames.X post import)

def f():
    print(X)                 # Access global X per LEGB lookup

def g():
    X = 22                   # Local (function) X (hides module X)
    print(X)

class C:
    X = 33                   # Class attribute C.X (self.X pre self.m())
    def m(self):
        X = 44               # Local (function) X in method (unused here)
        self.X = 55          # Instance attribute self.X (hides class X)

if __name__ == '__main__':
    print(X)                 # 11: module (a.k.a. manynames.X outside file)
    f()                      # 11: global
    g()                      # 22: local
    print(X)                 # 11: module name unchanged

    I = C()                  # Make instance
    print(I.X)               # 33: class name inherited by instance
    I.m()                    # Attach attribute name X to instance now
    print(I.X)               # 55: instance
    print(C.X)               # 33: class (a.k.a. I.X if no X in I)

    #print(C.m.X)            # FAILS: only visible in method
    #print(g.X)              # FAILS: only visible in function

