"""
Test the rangetest decorator (usage differs from rangetest0).
Comment lines raise TypeError unless "python -O" or similar in compileall.
"""
from rangetest import rangetest
def announce(what): print(what.center(24, '-'))   # str method

# Test functions, positional and keyword
announce('Functions')

@rangetest(age=(0, 120))                  # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print(f'{name} is {age} years old')

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2024))
def birthday(M, D, Y):
    print(f'birthday = {M}/{D}/{Y}')

persinfo('Pat', 40)
persinfo(age=40, name='Pat')
birthday(8, D=31, Y=2024)
#persinfo('Pat', 150)
#persinfo(age=150, name='Pat')
#birthday(8, Y=2025, D=40)

# Test methods, positional and keyword
announce('Methods')

class Person:
    def __init__(self, name, job, pay):
        self.job  = job
        self.pay  = pay
                                          # giveRaise = rangetest(...)(giveRaise)
    @rangetest(percent=(0.0, 1.0))        # percent passed by name or position
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

sue = Person('Sue Jones', 'dev', 100_000)
bob = Person('Bob Smith', 'dev', 100_000)
sue.giveRaise(percent=.20)
bob.giveRaise(.10)
print(f'sue=>{sue.pay}, bob=>{bob.pay}')
#sue.giveRaise(1.20)
#bob.giveRaise(percent=1.20)

# Test omitted defaults: skipped
announce('Defaults')

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)

omitargs(1, 2, 3, 4)           # Positionals
omitargs(1, 2, 3)              # Default d
omitargs(1, 2, 3, d=4)         # Keyword d
omitargs(1, d=4)               # Default b and c
omitargs(d=4, a=1)             # Ditto
omitargs(1, b=2, d=4)          # Default c
omitargs(d=8, c=7, a=1)        # Default b

#omitargs(1, 2, 3, 11)         # Bad d
#omitargs(1, 2, 11)            # Bad c
#omitargs(1, 2, 3, d=11)       # Bad d
#omitargs(11, d=4)             # Bad a
#omitargs(d=4, a=11)           # Bad a
#omitargs(1, b=11, d=4)        # Bad b
#omitargs(d=8, c=7, a=11)      # Bad a

