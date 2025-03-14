class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

bob = Person('Bob Smith')                         # Test the class
sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
print(bob.name, bob.pay)                          # Fetch attached attributes
print(sue.name, sue.pay)                          # sue's and bob's attrs differ

