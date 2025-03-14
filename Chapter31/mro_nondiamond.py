class E:       attr = 'E'     #   D     E
class D:       attr = 'D'     #   |     |
class C(E):    attr = 'C'     #   B     C
class B(D):    pass           #    \   /
class A(B, C): pass           #      A
                              #      |
X = A()                       #      X
print(X.attr)  # D

