class tracer(object):
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):                # On method fetch
        def wrapper(*args, **kwargs):                  # Retain both inst
            return self(instance, *args, **kwargs)     # Runs __call__
        return wrapper


@tracer
def hack(a, b, c):                           # hack = tracer(hack)
    print(a + b + c)                         # Uses __call__ only

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay
    @tracer                                  # giveRaise = tracer(giveRaise)
    def giveRaise(self, percent):            # Makes giveRaise a descriptor
        self.pay *= (1.0 + percent)

