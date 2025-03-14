"""
Class decorator with Private attribute declarations.

Privacy for attributes fetched from class instances.
See self-test code at end of file for a usage example.

Rebinding is: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a new Doubler instance.
"""

traceMe = False
def trace(*args):
    if traceMe: print(f'[{' '.join(map(str, args))}]')   # Python 3.12+ f-string

def Private(*privates):                              # privates in enclosing scope
    def onDecorator(aClass):                         # aClass in enclosing scope
        class onInstance:                            # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):             # My attrs don't call getattr
                trace('get:', attr)                  # Others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch, ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):             # Outside accesses
                trace('set:', attr, value)                  # Others run normally
                if attr == 'wrapped':                       # Allow my attrs
                    self.__dict__[attr] = value             # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change, ' + attr)
                else:
                    setattr(self.wrapped, attr, value)      # Wrapped obj attrs
        return onInstance
    return onDecorator


if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')                   # Doubler = Private(...)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                 # Accesses inside the subject class
            self.data  = start                 # Not intercepted: run normally
        def size(self):
            return len(self.data)              # Method bodies run with no checking
        def double(self):                      # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print(f'{self.label} => {self.data}')

    print('Making instances...')
    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])

    # The following all succeed properly

    print('\nExploring X instance...')
    print(X.label)                             # Accesses outside subject class
    X.display(); X.double(); X.display()       # Intercepted: validated, delegated

    print('\nExploring Y instance...')
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Hack'
    Y.display()

    # The following all fail properly
    """
    print(X.size())          # Prints "TypeError: private attribute fetch, size"
    print(X.data)
    X.data = [1, 1, 1]       # Prints "TypeError: private attribute change, data"
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    """

