# Registering decorated objects to an API
from __future__ import print_function # 2.X

registry = {}
def register(obj):                          # Both class and func decorator
    registry[obj.__name__] = obj            # Add to registry
    return obj                              # Return obj itself, not a wrapper

@register
def hack(x):
    return(x ** 2)                          # hack = register(hack)

@register
def app(x):
    return(x ** 3)

@register
class Code:                                 # Code = register(Code)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(hack(2))                              # Invoke objects manually
print(app(2))                               # Later calls not intercepted
X = Code(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](2))    # Invoke from registry


"""
Registry:
hack => <function hack at 0x10bf78fe0> <class 'function'>
app => <function app at 0x10bf79080> <class 'function'>
Code => <class '__main__.Code'> <class 'type'>

Manual calls:
4
8
16

Registry calls:
hack => 4
app => 8
Code => 16
"""
