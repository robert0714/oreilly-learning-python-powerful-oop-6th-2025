"""
Not listed (but run) in the book: additional iterator timings.
Partly redundant with the earlier timer_tests.py in the chapter,
though this verifies that its homegrown and timeit code agree.
"""

import pybench

stmts = [
# Use function calls: map wins
    (1000, 10, "res=[]\nfor x in 'hack' * 2500: res.append(ord(x))"),
    (1000, 10, "[ord(x) for x in 'hack' * 2500]"),
    (1000, 10, "list(map(ord, 'hack' * 2500))"),
    (1000, 10, "list(ord(x) for x in 'hack' * 2500)"),
]

pybench.runner(stmts, None, False)

