"""
Not in the book - another example of full paths' support for dual-mode files:

  $ export PYTHONPATH=.
  $ python3 system1/main.py                 # Program mode
  HACKHACKHACKHACK
  $ python3
  >>> from system1.utilities import name    # Package mode
  >>> name
  'HACK'
"""

from system1.utilities import name
print(name * 4)
