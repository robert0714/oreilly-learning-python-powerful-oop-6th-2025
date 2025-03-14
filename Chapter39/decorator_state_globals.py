calls = 0
def tracer(func):                         # State via enclosing scope and global
    def wrapper(*args, **kwargs):         # Instead of class attributes
        global calls                      # calls is global, not per-function
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@tracer
def hack(a, b, c):           # Same as: hack = tracer(hack)
    print(a + b + c)

@tracer
def code(x, y):              # Same as: code = tracer(code)
    print(x ** y)

if __name__ == '__main__':
    hack(1, 2, 3)            # Really calls wrapper, assigned to hack
    hack(a=4, b=5, c=6)      # wrapper calls hack

    code(4, 2)               # Really calls wrapper, assigned to code
    code(2, y=16)            # Global calls is not per-decoration here!

