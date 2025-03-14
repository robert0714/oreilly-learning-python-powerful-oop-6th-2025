"""
Implement intersection and union for one or more arguments.
Inputs may be any sort of iterable that supports multiple in
tests, and results are always lists.  This intersect avoids 
duplicates in results by in test, but may be slow: improve me.
"""

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

