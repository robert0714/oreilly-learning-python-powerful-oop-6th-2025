def rangetest(*argchecks):                  # Validate positional arg ranges
    def onDecorator(func):
        if not __debug__:                   # True if "python -O main.py args..."
            return func                     # No-op: call original directly
        else:                               # Else wrapper while debugging
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = f'Argument {ix} not in {low}..{high}'
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator

