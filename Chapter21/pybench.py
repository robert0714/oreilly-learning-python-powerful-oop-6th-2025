r"""
Time the speed of one or more Pythons on multiple code-string 
benchmarks with timeit.  This is a function, to allow timed tests
to vary.  It times all code strings in a passed list, in either:

1) The Python running this script, by timeit API calls
2) Multiple Pythons whose paths are passed in a list, by reading
   the output of timeit command lines run by os.popen that use 
   Python's -m switch to find timeit on the module search path

In command-line mode (2) only, this replaces all " in timed code
with ', to avoid clashes with argument quoting; splits multiline 
statements into one quoted argument per line so all will be run;
and replaces all \t in indentation with 4 spaces for uniformity.

Caveats: 
- Command-line mode (only) uses naive quoting and MAY FAIL if code
  embeds and requires double quotes; quoted code is incompatible 
  with the host shell; or command length exceeds shell limits.
- PyPy is largely unusable in command-line mode (2) today, as its
  modified timeit output in this mode is jarring in the report.
- This does not (yet?) support a setup statement in any mode: the
  time of all code in the test stmt is charged to its total time.
  
As fallbacks on fails, use either this module's API-call mode to 
test one Python at a time, or the homegrown timer.py module.
"""

import sys, os, time, timeit
defnum, defrep= 1000, 5    # May vary per stmt

def show_context(): 
    """
    Show run's context using an arguably gratuitous f-string
    that fails on 3.10 PyPy without "..." for nested ' quotes.
    """
    print(f"Python {'.'.join(str(x) for x in sys.version_info[:3])}"
          f' on {sys.platform}'
          f" at {time.strftime('%b-%d-%Y, %H:%M:%S')}")

def runner(stmts, pythons=None, tracecmd=False):
    """
    Main logic: run tests per input lists which determine usage modes.
    stmts:   [(number?, repeat?, stmt-string)]
    pythons: None=host python only, or [python-executable-paths]
    """
    show_context()
    for (number, repeat, stmt) in stmts:
        number = number or defnum
        repeat = repeat or defrep    # 0=default

        if not pythons:
            # Run stmt on this python: API call
            # No need to split lines or quote here
            best = min(timeit.repeat(stmt=stmt, number=number, repeat=repeat))
            print(f'{best:.4f}  {stmt[:70]!r}')

        else:
            # Run stmt on all pythons: command line
            # Split lines into quoted arguments
            print('-' * 80)
            print(repr(stmt))                                         # show quotes
            for python in pythons:
                stmt  = stmt.replace('"', "'")                        # all " => '
                stmt  = stmt.replace('\t', ' ' * 4)                   # tab => ____
                lines = stmt.split('\n')                              # line => arg
                args  = ' '.join(f'"{line}"' for line in lines)       # arg => "arg"

                oscmd = f'{python} -m timeit -n {number} -r {repeat} {args}'
                print(oscmd if tracecmd else python)
                print('\t' + os.popen(oscmd).read().rstrip())
