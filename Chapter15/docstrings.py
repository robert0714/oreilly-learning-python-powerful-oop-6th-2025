"""
Module documentation
This module defines a name, function and class.
"""

edition = 6

def square(x):
    r'''
    Function documentation
    Returns the \square\ of its \numeric\ argument.
    '''
    return x ** 2   # power operator

class PartVI:
    "Class documentation for \U0001F40D 👍"
    pass

# Top-level code
print(square(edition))
print(square.__doc__)
print(PartVI.__doc__)
