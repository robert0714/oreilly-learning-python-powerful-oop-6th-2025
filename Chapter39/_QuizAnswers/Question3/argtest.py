"""
A function decorator that performs arbitrary passed-in validations
for arguments passed to any function method.  Range and type tests 
are provided as two example uses; valuetest handles more arbitrary 
tests on an argument's value.

Arguments are specified by keyword to the decorator.  In the actual
call, arguments may be passed by position or keyword, and defaults
may be omitted.  See self-test scripts for example use cases.

Caveats: doesn't fully support nesting because call-proxy args
differ; doesn't validate extra args passed to a decoratee's *args;
and may be no easier than an assert except for provided use cases.
"""
trace = False


def rangetest(**argchecks):
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])

def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))

def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))


def argtest(argchecks, failif):             # Validate args per failif + criteria
    def onDecorator(func):                  # onCall retains func, argchecks, failif
        if not __debug__:                   # No-op if "python -O main.py args..."
            return func
        else:
            code = func.__code__
            expected = code.co_varnames[:code.co_argcount]

            def onError(argname, criteria):
                 errmsg = f'{func.__name__} argument "{argname}" not {criteria}'
                 raise TypeError(errmsg)

            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():      # For all to test
                    if argname in kargs:                           # Passed by name
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)

                    elif argname in positionals:                   # Passed by posit
                        position = positionals.index(argname)
                        if failif(pargs[position], criteria):
                            onError(argname, criteria)

                    else:                                          # Not passed-dflt
                        if trace:
                            print('Argument "%s" defaulted' % argname)
                return func(*pargs, **kargs)   # OK: run original call
            return onCall
    return onDecorator

