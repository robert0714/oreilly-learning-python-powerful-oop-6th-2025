from person_10 import Person                        # Example 28-10's Person

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)      # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)      # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)           # Delegate all other attrs

    def __repr__(self):
        return str(self.person)                     # Must overload again per ahead

if __name__ == '__main__':
    pat = Manager('Pat Jones', 50000)               # Embed a Person
    pat.giveRaise(.10)                              # Run Manager.giveRaise
    print(pat.lastName())                           # Delegate to embedded
    print(pat)                                      # Run Manager.__repr__

