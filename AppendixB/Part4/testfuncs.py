def f1(a, b): print(a, b)            # Normal args

def f2(a, *b): print(a, b)           # Positional collectors

def f3(a, **b): print(a, b)          # Keyword collectors

def f4(a, *b, **c): print(a, b, c)   # Mixed modes

def f5(a, b=2, c=3): print(a, b, c)  # Defaults

def f6(a, b=2, *c): print(a, b, c)   # Defaults and positional collector

