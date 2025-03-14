# >>> from reverse import *
# >>> rev1('hack')

def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1])        # Recursive

def rev2(S):
    return ''.join(reversed(S))            # Nonrecursive iterable
        
def rev3(S):
    return S[::-1]                         # Sequence reversal by slice        

