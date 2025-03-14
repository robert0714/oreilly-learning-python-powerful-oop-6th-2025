"Test the argtest decorator on function calls"

import sys
from argtest import rangetest, typetest, valuetest

def fails(test):
    try:    result = test()
    except: print('[%r]' % sys.exception())
    else:   print('?%s?' % result)

print('--------------------------------------------------------------------')

# Canned use cases: ranges, types

@rangetest(m=(1, 12), d=(1, 31), y=(1900, 2013))
def date(m, d, y):
    print(f'date = {m}/{d}/{y}')

date(1, 2, 1960)
fails(lambda: date(1, 2, 3))

@typetest(a=int, c=float)
def sum(a, b, c, d):
    print(a + b + c + d)

sum(1, 2, 3.0, 4)
sum(1, d=4, b=2, c=3.0)
fails(lambda: sum('hack', 2, 99, 4))
fails(lambda: sum(1, d=4, b=2, c=99))

print('--------------------------------------------------------------------')

# Arbitrary/mixed tests

@valuetest(word1=str.islower, word2=(lambda x: x[0].isupper()))
def msg(word1='sixth', word2='Edition', label='The'):
    print('%s %s %s' % (label, word1, word2))

msg()  # word1 and word2 defaulted
msg('code', 'Hack')
fails(lambda: msg('Python', 'Decorators'))
fails(lambda: msg('python', word2='decorators'))

print('--------------------------------------------------------------------')

# Manual type and range tests

@valuetest(A=lambda x: isinstance(x, int), B=lambda x: x > 0 and x < 10)
def manual(A, B):
    print(A + B)

manual(100, 2)
fails(lambda: manual(1.99, 2))
fails(lambda: manual(100, 20))

print('--------------------------------------------------------------------')

# Nesting: runs both, by nesting proxies on original.
# Open issue: outer levels do not validate positionals due
# to call proxy function's differing argument signature;
# when trace=True, in all but the last of these "X" is
# classified as defaulted due to the proxy's signature.

@rangetest(X=(1, 10))
@typetest(Z=str)                      # Only innermost validates positional args
def nester(X, Y, Z):
    return('%s-%s-%s' % (X, Y, Z))

print(nester(1, 2, 'lp6e'))                # Original function runs properly
fails(lambda: nester(1, 2, 3))             # Nested typetest is run:  positional
fails(lambda: nester(1, 2, Z=3))           # Nested typetest is run:  keyword
fails(lambda: nester(0, 2, 'lp6e'))        # <==Outer rangetest not run: posit.
fails(lambda: nester(X=0, Y=2, Z='lp6e'))  # Outer rangetest is run:  keyword

