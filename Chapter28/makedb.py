from person_14 import Person, Manager            # Load our classes
bob = Person('Bob Smith')                        # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
pat = Manager('Pat Jones', 50000)

import shelve
db = shelve.open('persondb')                     # Filename where objects are stored
for obj in (bob, sue, pat):                      # Use object's name attr as key
    db[obj.name] = obj                           # Store object in shelf by key
db.close()                                       # Close after making changes

