def sumtree(L, trace=False):
    tot = 0
    for x in L:                                 # For each item at this level
        if not isinstance(x, list):
            tot += x                            # Add numbers directly
            if trace: print(x, end=', ')
        else:
            tot += sumtree(x, trace)            # Recur for sublists
    return tot

