"""
mydir.py: a module that lists the namespaces of other modules.
Import this module's listing and pass an imported module, or 
run this file as a script to perform its self-test code.
"""

sepchr = '-'
seplen = 60

def listing(module, verbose=True, unders=True):
    """
    List module: just attributes if verbose=False, 
    hide built-in __X__ attributes if unders=False. 
    """
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print(f'name: {module.__name__}\nfile: {module.__file__}')
        print(sepline)

    # Scan namespace keys
    for (count, attr) in enumerate(sorted(module.__dict__)):
        prefix = f'{count + 1:02d}) {attr}'
        if attr.startswith('__'):
            if unders:
                print(prefix, '<built-in name>')    # Skip __file__, etc.
        else:
            print(prefix, getattr(module, attr))    # Or module.__dict__[attr]

    if verbose:
        print(sepline)
        print(f'{module.__name__} has {count + 1} names')
        print(sepline)

if __name__ == '__main__':
    import mydir
    listing(mydir)                                  # Self-test code: list myself

