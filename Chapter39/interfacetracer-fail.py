class Tracer:
    def __init__(self, aClass):               # On @decorator
        self.aClass = aClass                  # Use instance attribute
    def __call__(self, *args):                # On instance creation
        self.wrapped = self.aClass(*args)     # ONE (LAST) INSTANCE PER CLASS!
        return self
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

@Tracer                                       # Triggers __init__
class Hack:                                   # Like: Hack = Tracer(Hack)
    def display(self):
        print('Hack!' * 3)

work = Hack()                                 # Triggers __call__
work.display()                                # Triggers __getattr__

@Tracer
class Person:                                 # Person = Tracer(Person)
    def __init__(self, name):                 # Person rebound to a Tracer
        self.name = name

bob = Person('Bob')                           # bob is really a Tracer
print(bob.name)                               # Tracer embeds a Person
sue = Person('Sue')
print(sue.name)                               # sue overwrites bob
print(bob.name)                               # OOPS: now bob's name is 'Sue'!

