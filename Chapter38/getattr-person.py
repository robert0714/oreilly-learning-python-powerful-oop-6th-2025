class Person:
    def __init__(self, name):               # On [Person()]
        self._name = name                   # Triggers __setattr__!

    def __getattr__(self, attr):            # On [obj.undefined]
        print('get: ' + attr)
        if attr == 'name':                  # Intercept name: not stored
            return self._name               # Does not loop: real attr
        else:                               # Others are errors
            raise AttributeError(attr)

    def __setattr__(self, attr, value):     # On [obj.any = value]
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                  # Set internal name
        self.__dict__[attr] = value         # Avoid looping here

    def __delattr__(self, attr):            # On [del obj.any]
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                  # Avoid looping here too
        del self.__dict__[attr]             # but much less common

sue = Person('Sue Jones')           # sue has a managed attribute
print(sue.name)                     # Runs __getattr__
sue.name = 'Susan Jones'            # Runs __setattr__
print(sue.name)
del sue.name                        # Runs __delattr__

print('-'*20)
bob = Person('Bob Smith')           # bob's attrs work like sue's
print(bob.name)
#print(Person.name.__doc__)         # No direct equivalent here!

