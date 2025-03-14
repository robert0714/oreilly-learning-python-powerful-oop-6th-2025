X = 11                        # My X: global to this file only

import lex1                   # Gain access to names in lex1
lex1.f()                      # Sets lex1.X, not this file's X
print(X, lex1.X)

