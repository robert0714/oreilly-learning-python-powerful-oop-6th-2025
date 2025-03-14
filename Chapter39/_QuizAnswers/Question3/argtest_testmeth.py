"Test the argtest decorator on method calls"

import sys
from argtest import rangetest, typetest

class C:
    @rangetest(a=(1, 10))
    def meth1(self, a):
        return a * 1000

    @typetest(a=int)
    def meth2(self, a):
        return a * 1000

X = C()
print(X.meth1(5))                      # 5000

try:
    X.meth1(20)
except:
    print(repr(sys.exception()))      # TypeError('meth1 argument "a" not (1, 10)')

print(X.meth2(20))                    # 20000

try:
    X.meth2(20.9)
except:
    print(repr(sys.exception()))      # TypeError('meth2 argument "a" not <class \'int\'>')

