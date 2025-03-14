"Simplistic timing function"

import time
def timer(func, *args):                    # Any positional arguments (only)
    start = time.perf_counter()
    for i in range(100_000):               # Hardcoded reps, range() timed
        func(*args)
    return time.perf_counter() - start     # Total elapsed time in seconds
