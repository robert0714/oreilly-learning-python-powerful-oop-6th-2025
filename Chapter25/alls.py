__all__ = ['a', '_c']                  # Control from * exports, take 2
a, b, _c, _d = 1, 2, 3, 4              # __all__ has precedence over _X

