# Not listed in the book: nest the decorator's class

class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        'name descriptor docs'

        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()                       # Assign descriptor to attr

sue = Person('Sue Jones')               # sue has a managed attribute
print(sue.name)                         # Runs Name.__get__
sue.name = 'Susan Jones'                # Runs Name.__set__
print(sue.name)
del sue.name                            # Runs Name.__delete__

print('-'*20)
bob = Person('Bob Smith')               # bob inherits descriptor too
print(bob.name)
print(Person.Name.__doc__)               # <== Differs: class moved into Person

