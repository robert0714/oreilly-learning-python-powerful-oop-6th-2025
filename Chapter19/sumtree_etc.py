# Test book's sumtrees plus an additional coding

more = lambda x: None
note = lambda q, x: print(x, end=', ') if q else None
from sumtree_tester import tester



# Breadth-first by items: add to end

def sumtree(L, trace=False):                     # Breadth-first, explicit queue
    tot = 0
    items = list(L)                              # Start with copy of top level
    while items:
        more(items)
        front = items.pop(0)                     # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                         # Add numbers directly
            note(trace, front)
        else:
            items.extend(front)                  # <== Append all in nested list
    return tot

tester(sumtree)
print('-'*40)



# Depth-first by items: add to front (like recursive calls version)

def sumtree(L, trace=False):                     # Depth-first, explicit stack
    tot = 0
    items = list(L)                              # Start with copy of top level
    while items:
        more(items)
        front = items.pop(0)                     # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                         # Add numbers directly
            note(trace, front)
        else:
            items[:0] = front                    # <== Prepend all in nested list
    return tot

tester(sumtree)
print('-'*40)



# Breadth-first by levels (alternative coding)

def sumtree(L, trace=True):
    tot = 0
    levels = [L]
    while levels:
        more(levels)
        front = levels.pop(0)                    # Fetch/delete front path
        for x in front:
            if not isinstance(x, list):
                tot += x                         # Add numbers directly
                note(trace, x)
            else:
                levels.append(x)                 # Push/schedule nested lists
    return tot

tester(sumtree)
print('-'*40)



"""
Expected output:

1, 6, 2, 5, 7, 8, 3, 4, 36
1, 2, 3, 4, 5, 15
5, 4, 3, 2, 1, 15
----------------------------------------
1, 2, 3, 4, 5, 6, 7, 8, 36
1, 2, 3, 4, 5, 15
1, 2, 3, 4, 5, 15
----------------------------------------
1, 6, 2, 5, 7, 8, 3, 4, 36
1, 2, 3, 4, 5, 15
5, 4, 3, 2, 1, 15
----------------------------------------
"""
