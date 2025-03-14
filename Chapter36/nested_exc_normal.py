def action3():
    print(1 + [])              # Generate TypeError

def action2():
    try:                       # Most recent matching try
        action3()
    except TypeError:          
        print('Inner try')     # Match kills the exception
        raise                  # Unless manually reraised

def action1():
    try:
        action2()
    except TypeError:
        print('Outer try')     # Run only if action2 reraises

if __name__ == '__main__': action1()

