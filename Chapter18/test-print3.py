from print3 import print3
print3(1, 2, 3)                         # Defaults
print3(1, 2, 3, sep='')                 # Suppress separator
print3(1, 2, 3, sep='...')              # Custom separator
print3(1, [2], (3,), sep='...')         # Various object types

print3(4, 5, 6, sep='', end='')         # Suppress newline
print3(7, 8, 9)                         # Finish line
print3()                                # Blank line

import sys
print3(1, 2, 3, sep='?', end='.\n', file=sys.stderr)    # Redirect to stderr

print3('LP6E was here', file=open('log.txt', 'w'))      # Redirect to a file
print3(open('log.txt').read())

