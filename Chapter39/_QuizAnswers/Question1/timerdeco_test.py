"""
Test the call-timer decorator on functions and methods.
Sleeps have been added to scale up some too-fast calls.
"""

import sys, time
from timerdeco import timer


print('Functions-------------------------------------------------')
# Test on functions

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                               # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]           # listcomp(...) triggers onCall

@timer('[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N))) 

for func in (listcomp, mapcall):
    result = func(5)                           # Time for this call, all calls, return value
    func(5_000_000)
    print(result)
    print(f'allTime = {func.alltime:.5f}\n')   # Total time for all calls


print('Methods---------------------------------------------------')
# Test on methods

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @timer(label='$$')
    def giveRaise(self, percent):            # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)          # tracer remembers giveRaise
        time.sleep(0.25)

    @timer(label='@@')
    def lastName(self):                      # lastName = timer(...)(lastName)
        time.sleep(0.25)
        return self.name.split()[-1]         # alltime per class, not instance

sue = Person('Sue Jones', 100_000)
bob = Person('Bob Smith', 50_000)
sue.giveRaise(.20)                           # runs onCall(sue, .10)
bob.giveRaise(.10)

print(f'{int(sue.pay)=}, {int(bob.pay)=}')
print(f'{sue.lastName()=}, {bob.lastName()=}')    # runs onCall(sue), remembers lastName

print(f'{Person.giveRaise.alltime=:.5f}, {Person.lastName.alltime=:.5f}')

