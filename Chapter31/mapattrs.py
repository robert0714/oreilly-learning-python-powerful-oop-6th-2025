"""
Main tool: mapattrs() maps all attributes on or inherited by an
instance to the instance or class from which they are inherited.
Also here: assorted dictionary tools using comprehensions.

Assumes dir() gives all attributes of an instance.  To emulate 
inheritance, this uses the class's __mro__ tuple, which gives the
MRO search order for classes in Python 3.X.  A recursive tree
traversal for the DFLR order of classes is included but unused.
"""

import pprint
def trace(label, X, end='\n'):
    print(f'{label}\n{pprint.pformat(X)}{end}')   # Print nicely

def filterdictvals(D, V):
    """
    dict D with entries for value V removed.
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b': 2}
    """
    return {K: V2 for (K, V2) in D.items() if V2 != V}

def invertdict(D):
    """
    dict D with values changed to keys (grouped by values).
    Values must all be hashable to work as dict/set keys.
    invertdict(dict(a=1, b=2, c=1)) => {1: ['a', 'c'], 2: ['b']}
    """
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}

def dflr(cls):
    """
    Depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes.
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    """
    Inheritance order sequence: MRO or DFLR.
    DFLR alone is no longer used in Python 3.X.
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)

def mapattrs(instance, withobject=False, bysource=False):
    """
    dict with keys giving all inherited attributes of instance,
    with values giving the object that each is inherited from.
    withobject: False=remove object built-in class attributes.
    bysource:   True=group result by objects instead of attributes.
    Supports classes with slots that preclude __dict__ in instances.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
             if hasattr(obj, '__dict__') and attr in obj.__dict__:    # Slots okay
               attr2obj[attr] = obj
               break

    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)

if __name__ == '__main__':

    class D:         attr2 = 'D'
    class C(D):      attr2 = 'C'
    class B(D):      attr1 = 'B'
    class A(B, C):   pass
    I = A()
    I.attr0 = 'I'

    print(f'Py=>{I.attr0=}, {I.attr1=}, {I.attr2=}\n')    # Python's search
    trace('INHERITANCE', inheritance(I))                  # [Inheritance order]
    trace('ATTRIBUTES',  mapattrs(I))                     # {Attr => Source}
    trace('SOURCES',     mapattrs(I, bysource=True))      # {Source => [Attrs]}

