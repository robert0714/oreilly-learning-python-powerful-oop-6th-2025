def tracer(func):                        # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        wrapper.calls += 1
        print(f'call {wrapper.calls} to {func.__name__}')
        return func(*args, **kwargs)
    wrapper.calls = 0
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
    code(2, y=16)            # wrapper.calls _is_ per-decoration here

