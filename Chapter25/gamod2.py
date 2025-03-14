var = 2                                   # Real attribute returned directly

def __getattr__(name):                    # Undefined attr fetches routed here
    print(f'(virtual {name})', end=' ')
    match name:
        case 'test':
            return name * var
        case 'hack' | 'code':
            return name.upper()
        case _:
            raise AttributeError(f'{name} is undefined')

def __dir__():
    return ['var', 'test', 'hack', 'code']

print(test)                # File: does NOT call __getattr__ (raises NameError)
