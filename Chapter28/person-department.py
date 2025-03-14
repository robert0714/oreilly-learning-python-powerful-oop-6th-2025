from person_10 import Person, Manager           # Example 28-10's classes

class Department:
    def __init__(self, *args):
        self.members = list(args)               # Manage an objects list

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):              # Apply methods to all objects
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):                          # Display all nested objects
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    pat = Manager('Pat Jones', 50000)

    development = Department(bob, sue)          # Embed objects in a composite
    development.addMember(pat)
    development.giveRaises(.10)                 # Runs embedded objects' giveRaise
    development.showAll()                       # Runs embedded objects' __repr__

