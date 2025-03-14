class C2: ...                 # Make class objects (ovals)
class C3: ...
class C1(C2, C3): ...         # Linked to superclasses - in this order

I1 = C1()                     # Make instance objects (rectangles)
I2 = C1()                     # Linked to their class

