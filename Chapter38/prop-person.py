class Person: 
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, 'name property docs')

sue = Person('Sue Jones')           # sue has a managed attribute
print(sue.name)                     # Runs getName
sue.name = 'Susan Jones'            # Runs setName
print(sue.name)
del sue.name                        # Runs delName

print('-'*20)
bob = Person('Bob Smith')           # bob inherits property too
print(bob.name)
print(Person.name.__doc__)          # Or help(Person.name)

