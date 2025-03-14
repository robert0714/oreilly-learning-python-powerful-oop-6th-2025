# (Not in book) Same, but using super() instead of class-name calls for constructors

class Employee:
    def __init__(self, name, salary=0):
        self.name   = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary += self.salary * percent
    def work(self):
        print(self.name, 'does stuff')
    def __repr__(self):
        return (f'<{self.__class__.__name__}: '
                f'name="{self.name}", salary={self.salary:,.2f}>')

class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)
    def work(self):
        print(self.name, 'makes food')

class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)
    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)
    def work(self):
        print(self.name, 'makes pizza')

if __name__ == '__main__':
    pat = PizzaRobot('pat')       # Make a robot named pat
    print(pat)                    # Run inherited __repr__
    pat.work()                    # Run type-specific action
    pat.giveRaise(0.20)           # Give pat a 20% raise
    print(pat); print()

    for klass in Employee, Chef, Server, PizzaRobot:
        object = klass(klass.__name__)
        object.work()

