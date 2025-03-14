class tracer:
    def __init__(self, func):         # On @ decoration: save original func
        self.calls = 0
        self.func = func
    def __call__(self, *args):        # On later calls: run original func
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        self.func(*args)

@tracer
def hack(a, b, c):           # hack = tracer(hack)
    print(a + b + c)         # Wraps hack in a decorator object

