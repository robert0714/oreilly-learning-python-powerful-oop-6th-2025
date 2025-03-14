X = 1

def nester():
   X = 2                    # Hides global
   print(X)                 # Local: 2
   class C:
       print(X)             # In enclosing def (nester): 2
       def method1(self):
           print(X)         # In enclosing def (nester): 2
       def method2(self):
           X = 3            # Hides enclosing (nester)
           print(X)         # Local: 3
   I = C()
   I.method1()
   I.method2()

print(X)                    # Global: 1
nester()                    # Rest: 2, 2, 2, 3

