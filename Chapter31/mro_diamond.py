class D:       attr = 'D'     #      D
class C(D):    attr = 'C'     #    /   \
class B(D):    pass           #   B     C
class A(B, C): pass           #    \   /
                              #      A
X = A()                       #      |
print(X.attr)  # C            #      X

