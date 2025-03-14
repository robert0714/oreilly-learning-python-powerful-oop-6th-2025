class tracer:
    def __init__(self, func):          # Remember original, init counter
        self.calls = 0
        self.func  = func
    def __call__(self, *args):         # On later calls: add logic, run original
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args)

@tracer                                # Same as hack = tracer(hack)
def hack(a, b, c):                     # Wrap hack in a decorator object
    return a + b + c

if __name__ == '__main__':
    print(hack(1, 2, 3))               # Really calls the tracer wrapper object
    print(hack('a', 'b', 'c'))         # Invokes __call__ in class

