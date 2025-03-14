"""
File access_builtins.py (from Example 39-22, access_builtins_mixin_desc.py).
Route some implicit built-in operation fetches back to proxy class __getattr__, 
so they work the same as explicit by-name calls.  Expand list as needed to 
include other __X__ names used by proxied objects.
"""

class BuiltinsMixin:
    class ProxyDesc:                                          # Define descriptor
        def __init__(self, attrname):
            self.attrname = attrname
        def __get__(self, instance, owner):
            return instance.__getattr__(self.attrname)        # Run validations

    builtins = ['add', 'str', 'getitem', 'call']              # Plus any others
    for attr in builtins:
        exec(f'__{attr}__ = ProxyDesc("__{attr}__")')         # Make descriptors


