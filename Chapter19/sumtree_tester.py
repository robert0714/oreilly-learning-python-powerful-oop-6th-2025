tests = (
[1, [2, [3, 4], 5], 6, [7, 8]],      # Mixed nesting => 36
[1, [2, [3, [4, [5]]]]],             # Right-heavy nesting => 15
[[[[[1], 2], 3], 4], 5])             # Left-heavy nesting => 15

def tester(sumtree, trace=True):
    for test in tests:
        print(sumtree(test, trace))

