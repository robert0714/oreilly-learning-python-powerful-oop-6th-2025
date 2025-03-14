X = 1
import nest2

print(X, end=' ')             # My global X
print(nest2.X, end=' ')       # nest2's X
print(nest2.nest3.X)          # Nested nest3's X

