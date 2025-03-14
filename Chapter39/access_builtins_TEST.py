from importlib import import_module
def xprint(msg):
    x, y = msg.split()
    print(x.ljust(10), y)

mods = ['access_builtins_' + scheme
    for scheme in ('inline_direct', 'mixin_direct', 'mixin_getattr', 'mixin_desc')]

for modname in mods:
    modobj = import_module(modname)
    print(modobj.__name__.center(48, '-'))
    
    @modobj.Private('sum')                        # Add '__add__' to see if/how it's validated
    class Tally:                                  # Disable @ altogether to see default case
        def __init__(self):
            self.sum = 0
        def __add__(self, add):
            self.sum += add

    X = Tally()

    try:    X.sum
    except: xprint('sum failed')
    else:   xprint('sum worked')

    try:    X.__add__(5)
    except: xprint('__add__ failed')
    else:   xprint('__add__ worked')

    try:    X + 5
    except: xprint('+ failed')
    else:   xprint('+ worked')

    try:    assert X._onInstance__wrapped.sum == 10
    except: xprint('__wrapped failed')
    else:   xprint('__wrapped worked')

    try:    assert X._wrapped.sum == 10
    except: xprint('_wrapped failed')
    else:   xprint('_wrapped worked')


"""
==============================================================================================
Expected output


# WITHOUT __add__

$ py3 access_builtins_TEST.py
---------access_builtins_inline_direct----------
sum        failed
__add__    worked
+          worked
__wrapped  worked
_wrapped   failed
----------access_builtins_mixin_direct----------
sum        failed
__add__    worked
+          worked
__wrapped  failed
_wrapped   worked
---------access_builtins_mixin_getattr----------
sum        failed
__add__    worked
+          worked
__wrapped  worked
_wrapped   failed
-----------access_builtins_mixin_desc-----------
sum        failed
__add__    worked
+          worked
__wrapped  worked
_wrapped   failed


# WITH __add__

$ py3 access_builtins_TEST.py
---------access_builtins_inline_direct----------
sum        failed
__add__    worked
+          worked
__wrapped  worked
_wrapped   failed
----------access_builtins_mixin_direct----------
sum        failed
__add__    worked
+          worked
__wrapped  failed
_wrapped   worked
---------access_builtins_mixin_getattr----------
sum        failed
__add__    failed
+          failed
__wrapped  failed
_wrapped   failed
-----------access_builtins_mixin_desc-----------
sum        failed
__add__    failed
+          failed
__wrapped  failed
_wrapped   failed


# NO DECORATOR

$ py3 access_builtins_TEST.py
---------access_builtins_inline_direct----------
sum        worked
__add__    worked
+          worked
__wrapped  failed
_wrapped   failed
----------access_builtins_mixin_direct----------
sum        worked
__add__    worked
+          worked
__wrapped  failed
_wrapped   failed
---------access_builtins_mixin_getattr----------
sum        worked
__add__    worked
+          worked
__wrapped  failed
_wrapped   failed
-----------access_builtins_mixin_desc-----------
sum        worked
__add__    worked
+          worked
__wrapped  failed
_wrapped   failed

==============================================================================================
"""
