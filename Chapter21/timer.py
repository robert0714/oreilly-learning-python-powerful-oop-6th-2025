"""
Homegrown timing tools for arbitrary function calls.
Times one call, total of N, best of N, and best of totals of N.
Pass any number of positional and keyword arguments for each func. 
"""

import time
timer = time.perf_counter                         # See also time.process_time()

def once(func, *pargs, **kargs):                  # Collect arguments for func
    """
    Time to run func(...) one time.
    Returns (time, result).
    """
    start   = timer()
    result  = func(*pargs, **kargs)               # Unpack arguments for func
    elapsed = timer() - start
    return (elapsed, result)                      # Return result to verify

def total(reps, func, *pargs, **kargs):           # Collect arguments for func
    """
    Total time to run func(...) reps times.
    Returns (total-time, last-result).
    """
    total = 0                                     # Don't charge range() time
    for i in range(reps):
        time, result = once(func, *pargs, **kargs)
        total += time
    return (total, result)                        # Return last result to verify

def bestof(reps, func, *pargs, **kargs):
    """
    Best time among reps runs of func(...).
    Returns (best-time, best-time-result).
    """
    return min(once(func, *pargs, **kargs) for i in range(reps))

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best total time among reps1 runs of [reps2 runs of func(...)].
    Returns (best-total-time, best-total-time-last-result).
    """
    return min(total(reps2, func, *pargs, **kargs) for i in range(reps1))
