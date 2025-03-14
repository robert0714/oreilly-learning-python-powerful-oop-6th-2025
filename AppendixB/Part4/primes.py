def prime(y):
    if y <= 1:                                       # For some y > 1
        print(y, 'is nonprime')
    else:
        x = y // 2                                   # But / fails
        while x > 1:
            if y % x == 0:                           # No remainder?
                print(y, 'has factor', x)
                break                                # Skip else
            x -= 1
        else:
            print(y, 'is prime')

tests = (27, 24, 13, 13.0, 15, 15.0, 3, 2, 1, -3)
for test in tests:
    prime(test)

