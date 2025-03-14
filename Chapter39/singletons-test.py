from singletons1 import singleton

@singleton                                      # Person = singleton(Person)
class Person:                                   # Rebinds Person to onCall
     def __init__(self, name, hours, rate):     # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate
     def pay(self):
        return self.hours * self.rate

@singleton                                      # Hack = singleton(Hack)
class Hack:                                     # Rebinds Hack to onCall
    def __init__(self, val):                    # onCall remembers Hack
        self.attr = val

sue = Person('Sue', 50, 20)                     # Really calls onCall
print(sue.name, sue.pay())

bob = Person('Bob', 40, 10)                     # Same, single object
print(bob.name, bob.pay())

X = Hack(val=42)                                # One Person, one Hack
Y = Hack(99)
print(X.attr, Y.attr)

