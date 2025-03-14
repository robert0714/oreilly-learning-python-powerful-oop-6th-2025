import time

def timer(label='', trace=True):                  # On decorator args: retain args
    class Timer:
        def __init__(self, func):                 # On @: retain decorated func
            self.func    = func
            self.alltime = 0
        def __call__(self, *args, **kargs):       # On calls: call original
            start   = time.perf_counter()
            result  = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                if label: print(label, end=' ')
                print(f'{self.func.__name__}: {elapsed:.5f}, {self.alltime:.5f}')
            return result
    return Timer

