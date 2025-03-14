"""
Alternative intersection algorithm and tests (not in book)

================================================================================

Results (see Chapter 21):

>>> min(timeit.repeat("from inter3 import intersect; intersect('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.005092659033834934
>>> min(timeit.repeat("from inter3 import intersect; intersect('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.005093390122056007
>>> min(timeit.repeat("from inter3 import intersect; intersect('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.005092829931527376

>>> min(timeit.repeat("from inter3 import intersectX; intersectX('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.0018285661935806274
>>> min(timeit.repeat("from inter3 import intersectX; intersectX('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.0018283897079527378
>>> min(timeit.repeat("from inter3 import intersectX; intersectX('HACKK'*100, 'CODE'*100, 'CASH'*100)", number=100, repeat=100))
0.0018289494328200817

================================================================================

>>> from inter3 import intersect, intersectX
>>> s1, s2, s3 = 'HACKK', 'CODE', 'CASH'
>>> 
>>> def tester(func, items, *, trace=True):
...        for i in range(len(items)):
...            items = items[1:] + items[:1]
...            if trace: print(items)
...            print(sorted(func(*items)))
... 
>>> tester(intersect, (s1, s2, s3))
('CODE', 'CASH', 'HACKK')
['C']
('CASH', 'HACKK', 'CODE')
['C']
('HACKK', 'CODE', 'CASH')
['C']
>>> tester(intersectX, (s1, s2, s3))
('CODE', 'CASH', 'HACKK')
['C']
('CASH', 'HACKK', 'CODE')
['C']
('HACKK', 'CODE', 'CASH')
['C']
================================================================================
"""

def intersectX(*args):
    res = []
    for x in args[0]:     
        if x not in res:
            res.append(x) 
    for other in args[1:]:
        for x in res.copy():
            if x not in other:
                res.remove(x) 
    return res


def intersect(*args):
    res = []
    for x in args[0]:                    # Scan first sequence
        if x in res: continue            # Skip duplicates in [0]
        for other in args[1:]:           # For all other args
            if x not in other: break     # Item in each one?
        else:                            # No: break out of loop
            res.append(x)                # Yes: add items to end
    return res


def union(*args):
    res = []
    for seq in args:                     # For all args
        for x in seq:                    # For all in this arg
            if not x in res:
                res.append(x)            # Add new items to result
    return res

