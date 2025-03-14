def Tracer(aClass):                                   # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)     # Use enclosing-scope name
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)               # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)    # Delegate to wrapped obj
    return Wrapper


if __name__ == '__main__':

    @Tracer
    class Hack:                                  # Hack = Tracer(Hack)
        def display(self):                       # Hack is rebound to Wrapper
            print('Hack!' * 3)

    @Tracer
    class Person:                                # Person = Tracer(Person)
        def __init__(self, name, hours, rate):   # Wrapper remembers Person
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):                           # Accesses outside class traced
            return self.hours * self.rate        # In-method accesses not traced

    work = Hack()                                # Triggers Wrapper()
    work.display()                               # Triggers __getattr__
    print([work.fetches])

    print()
    bob = Person('Bob', 40, 50)                  # bob is really a Wrapper
    print(bob.name)                              # Wrapper embeds a Person
    print(bob.pay())

    print()
    sue = Person('Sue', rate=100, hours=60)      # sue is a different Wrapper
    print(sue.name)                              # With a different Person
    print(sue.pay())

    print()
    print(bob.name)                              # bob's state != sue's state
    print(bob.pay())
    print('calls:', [bob.fetches, sue.fetches])  # Wrapper attrs are not traced

