"""
Run pybench.py to time one or more Pythons on multiple code strings.
Use command-line arguments (which appear in sys.argv) to select modes:  

<python> pybench_tests.py
    times just the hosting Python on all code listed in stmts below
python3 pybench_tests.py -a
    times all stmts in all pythons whose paths are listed below 
python3 pybench_tests.py -a -t
    same as -a, but also traces command lines in full

Edit stms below to change tested code, and edit pythons below to give 
paths of Python executables to be tested in -a mode.  To find a Python's 
path, start its REPL, run "import sys", and inspect "sys.executable".
"""

import pybench, sys

pythons = [
    '/Library/Frameworks/Python.framework/Versions/3.12/bin/python3',
    '/Users/me/Downloads/pypy3.10-v7.3.16-macos_x86_64/bin/pypy3',
]

stmts = [
# Iterations
    (0, 0, '[x ** 2 for x in range(1000)]'),                        # (num,rpt,stmt)
    (0, 0, 'res=[]\nfor x in range(1000): res.append(x ** 2)'),     # \n=multistmt
    (0, 0, 'list(map(lambda x: x ** 2, range(1000)))'),             # \n\t=indent
    (0, 0, 'list(x ** 2 for x in range(1000))'),
# String ops
    (0, 0, "s = 'hack' * 2500\nx = [s[i] for i in range(10_000)]"),
    (0, 0, "s = '?'\nfor i in range(10_000): s += '?'"),            # A PyPy loss!
]

tracecmd = '-t' in sys.argv                           # -t: trace command lines?
pythons  = pythons if '-a' in sys.argv else None      # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)              # Time pythons on all stmts
