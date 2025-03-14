# Not in the book: catching all attributes with __getattribute__.
# Except for built-in ops like print: they skip the instance...
# This must avoid loops with object.__getattribute__.

from person_10 import Person                        # Load current Person

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)      # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        object.__getattribute__(self, 'person').giveRaise(percent + bonus) 

    def __getattribute__(self, attr):
        print('=>', attr)
        if attr == 'giveRaise':
            return object.__getattribute__(self, attr)
        else:
            return getattr(object.__getattribute__(self, 'person'), attr)

    # Comment out the following to test __repr__ fetch: object default used
    def __repr__(self):
        print('-> repr')
        return str(object.__getattribute__(self, 'person'))

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    pat = Manager('Pat Jones', 50000)               # Job name set by class
    pat.giveRaise(.10)
    print(pat.lastName())
    print(pat)


