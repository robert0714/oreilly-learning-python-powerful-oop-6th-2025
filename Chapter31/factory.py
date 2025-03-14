def factory(aClass, *pargs, **kargs):        # Varargs tuple, dict
    return aClass(*pargs, **kargs)           # Call aClass

class Hack:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job  = job

object1 = factory(Hack)                      # Make a Hack object
object2 = factory(Person, 'Sue', 'dev')      # Make a Person object
object3 = factory(Person, name='Bob')        # Ditto, with keywords and default

