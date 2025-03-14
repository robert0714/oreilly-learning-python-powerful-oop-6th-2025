"""
Call-timer decorator for both functions and methods.
"""
import time

def timer(label='', trace=True):               # On decorator args: retain args
    def onDecorator(func):                     # On @: retain decorated func
        def onCall(*args, **kargs):            # On calls: call original
            start   = time.perf_counter()      # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.perf_counter() - start
            onCall.alltime += elapsed
            if trace:
                if label: print(label, end=' ')
                print(f'{func.__name__}: {elapsed:.5f}, {onCall.alltime:.5f}')
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

