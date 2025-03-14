# Paste one at a time, or stub others out with triple quotes...

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])           # Use ternary expression

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])  # Any type, assume one+

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)    # Use extended unpacking




# And later...

"""
def mysum(first, *rest):
        return first if not rest else first + mysum(*rest)
"""

"""
def mysum(L):
    if not L: return 0
    return nonempty(L)                  # Call a function that calls me

def nonempty(L):
    return L[0] + mysum(L[1:])          # Indirectly recursive
"""
