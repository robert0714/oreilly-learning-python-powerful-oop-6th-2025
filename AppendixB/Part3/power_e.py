X = 5
L = list(map(lambda x: 2 ** x, range(7)))      # Or [2 ** x for x in range(7)]
print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

