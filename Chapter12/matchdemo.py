# state = 1 or 
#   [1, 2, 3] or [0, 2, 3] or (1, 2, 3) or (0, 2, 3) or 
#   dict(a=1, b=2, c=3) or dict(a=0, b=2, c=3) or other

state = dict(a=0, b=2, c=3)

match state:
    case 1 | 2 | 3 as what:              # Match integer literals, what = 1
        print('or', what)

    case [1, 2, what]:                   # Match sequence (1), what = 3
        print('list', what)
    case [0, *what]:                     # Match sequence (0), what = [2, 3]
        print('list', what)

    case {'a': 1, 'b': 2, 'c': what}:    # Match mapping, what = 3
        print('dict', what)
    case {'a': 0, **what}:               # Match mapping, what = {'b': 2, 'c': 3}
        print('dict', what)

    case (1, 2, what):                   # Match sequence: same as [1, 2, what] 
        print('tuple', what)
    case (0, *what):                     # Match sequence: same as [0, *what]
        print('tuple', what)

    case _ as what:                      # Match all other, what = other
        print('other', what)
