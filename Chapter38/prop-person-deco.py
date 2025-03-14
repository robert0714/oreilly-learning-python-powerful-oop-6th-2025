class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):                 # name = property(name)
        'name property docs'
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):          # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):                 # name = name.deleter(name)
        print('remove...')
        del self._name

sue = Person('Sue Jones')           # sue has a managed attribute
print(sue.name)                     # Runs name getter (def name 1)
sue.name = 'Susan Jones'            # Runs name setter (def name 2)
print(sue.name)
del sue.name                        # Runs name deleter (def name 3)

print('-'*20)
bob = Person('Bob Smith')           # bob inherits property too
print(bob.name)
print(Person.name.__doc__)          # Or help(Person.name)

