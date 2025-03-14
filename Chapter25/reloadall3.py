"""
reloadall3.py: transitively reload nested modules.
Alternative coding: nonrecursive, explicit stack.
"""

import types
from reloadall import status, tryreload, tester

def transitive_reload(objects, visited):
    while objects:
        next = objects.pop()                        # Delete next item at end
        if (type(next) == types.ModuleType          # Is it a module object?
            and next not in visited):               # Not already reloaded?
            status(next)                            # Reload this, push attrs
            tryreload(next)
            visited.add(next)
            objects.extend(next.__dict__.values())

def reload_all(*args):
    transitive_reload(list(args), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3')                # Test: reload myself or arg

