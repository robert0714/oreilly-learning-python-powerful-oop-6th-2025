class tracer(object):                         # For methods, but not functions!
    def __init__(self, meth):                 # On @ decorator
        self.calls = 0                         
        self.meth  = meth
    def __get__(self, instance, owner):       # On method fetch
        def wrapper(*args, **kwargs):         # On method call: proxy with self+inst
            self.calls += 1
            print(f'call {self.calls} to {self.meth.__name__}')
            return self.meth(instance, *args, **kwargs)
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

