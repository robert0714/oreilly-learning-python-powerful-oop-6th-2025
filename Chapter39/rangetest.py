"""
A function decorator that performs range-test validation for
arguments passed to any function or method.  Usage synopsis:

    @rangetest(percent=(0.0, 1.0), month=(1, 12))
    def func-or-method(..., percent, ..., month=5, ...):
        ...
    func-or-method(..., value, month=8, ...)

Arguments are specified by keyword to the decorator. In the actual
call, arguments may be passed by position or keyword, and defaults
may be omitted.  See rangetest_test.py for example use cases.
"""
trace = True

def rangetest(**argchecks):                 # Validate ranges for both+defaults
    def onDecorator(func):                  # onCall remembers func and argchecks
        if not __debug__:                   # True if "python -O main.py args..."
            return func                     # Wrap if debugging; else use original
        else:
            funcname = func.__name__
            funccode = func.__code__
            funcargs = funccode.co_varnames[:funccode.co_argcount]

            def onCall(*pargs, **kargs):
                # All pargs match first N expected args by position
                # The rest must be in kargs or be omitted defaults
                positionals = funcargs[:len(pargs)]
                errormsg    = lambda *args: '%s argument "%s" not in %s..%s' % args

                for (argname, (low, high)) in argchecks.items():
                    # For all args to be checked
                    if argname in kargs:
                        # Was passed by name
                        if kargs[argname] < low or kargs[argname] > high:
                            raise TypeError(errormsg(funcname, argname, low, high))

                    elif argname in positionals:
                        # Was passed by position
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            raise TypeError(errormsg(funcname, argname, low, high))

                    else:
                        # Assume not passed: default
                        if trace:
                            print(f'-Argument "{argname}" defaulted')

                return func(*pargs, **kargs)    # OK: run original call
            return onCall
    return onDecorator

