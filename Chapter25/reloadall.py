"""
reloadall.py: transitively reload nested modules.
Call reload_all with one or more imported modules as arguments.
These modules, and all the modules they import, are reloaded.
"""

import types
from importlib import reload

def status(module):
    print('reloading', module.__name__)

def tryreload(module):
    try:
        reload(module)                                   # Imports might fail
    except:
        print('FAILED:', module)

def transitive_reload(module, visited):
    if not module in visited:                            # Trap cycles, duplicates
        status(module)                                   # Reload this module
        tryreload(module)                                # And visit children
        visited[module] = True
        for attrobj in module.__dict__.values():         # For all attrs in mod
            if type(attrobj) == types.ModuleType:        # Recur if nested module
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}                                         # Main entry point
    for arg in args:                                     # For all passed in
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):                           # Self-test: cmd or passed
    import importlib, sys                                # Imports for tests only
    if len(sys.argv) > 1:                                # Command-line argument?
        modname = sys.argv[1]
    module = importlib.import_module(modname)            # Import by name string
    reloader(module)                                     # Test passed-in reloader

if __name__ == '__main__':
    tester(reload_all, 'reloadall')                      # Test: reload self or arg

