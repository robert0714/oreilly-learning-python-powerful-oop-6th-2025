class tracer(object):                        # A decorator+descriptor
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func/meth
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):      # On method attribute fetch
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):          # Save both instances
        self.desc = desc                     # Route calls back to deco/desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)  # Runs tracer.__call__


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

