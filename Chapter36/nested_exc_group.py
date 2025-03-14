def action3():
    raise ExceptionGroup('Nest*', [IndexError(1), TypeError(2), SyntaxError(3)])

def action2():
    try:
        action3()
    except* IndexError:        # Consume matches, rest propagate
        print('Got IE')

def action1():
    try:
        action2()
    except* TypeError:         # Consume matches, rest propagate
        print('Got TE')

if __name__ == '__main__': action1()

