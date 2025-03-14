def countdown(N):
    if N == 0:
        print('stop')
    else:
        print(N, end=' ')
        countdown(N - 1)

def countdown2(N):                            # Generator function, recursive
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N - 1): yield x   # Or: yield from countdown2(N - 1)

