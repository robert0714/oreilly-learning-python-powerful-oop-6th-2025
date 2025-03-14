def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])       # Call myself recursively

