r"""
Emulate most of the Python 3.X print function as customizable code.
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout).
"""
import sys

def print3(*args, **kargs):
    sep  = kargs.get('sep', ' ')            # Keyword arg defaults
    end  = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''                             # Build+print a string
    first  = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

