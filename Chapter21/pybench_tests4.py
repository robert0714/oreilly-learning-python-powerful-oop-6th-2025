"""
Not listed or run in the book: additional iterator timings.
Redundant with the earlier timer_tests.py in the chapter.
Times are relatively the same but higher, due to range():

Python 3.12.2 on darwin at Jun-26-2024, 17:12:08
0.4558  'res=[]\nfor x in range(10_000): res.append(abs(x))'
0.3744  '[abs(x) for x in range(10_000)]'
0.2861  'list(map(abs, range(10_000)))'
0.5770  'list(abs(x) for x in range(10_000))'
"""

import pybench

stmts = [
# Use function calls: map wins
    (0, 0, 'res=[]\nfor x in range(10_000): res.append(abs(x))'),
    (0, 0, '[abs(x) for x in range(10_000)]'),
    (0, 0, 'list(map(abs, range(10_000)))'),
    (0, 0, 'list(abs(x) for x in range(10_000))'),
]

pybench.runner(stmts, None, False)

