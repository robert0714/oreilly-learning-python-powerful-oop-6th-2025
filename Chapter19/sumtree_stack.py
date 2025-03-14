def sumtree(L, trace=False):                     # Depth-first, explicit stack
    tot = 0
    items = list(L)                              # Start with copy of top level
    while items:
        front = items.pop(0)                     # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                         # Add numbers directly
            if trace: print(front, end=', ')
        else:
            items[:0] = front                    # <== Prepend all in nested list
    return tot

