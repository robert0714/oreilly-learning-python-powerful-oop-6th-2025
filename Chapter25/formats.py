"""
File: formats.py 
Various specialized string display formatting utilities.
Test me with canned self-test or command-line arguments.
To do: add parens for negative money, add more features.

LP6E: this example was cut from the book for space, and 
is included here only as a bonus self-study example.
Part of its point was to demo that you can write your
own tools instead of relying on built-ins, like the 
"," in format methods (and today, f-strings).  It's 
generally better to learn to fish than be given a fish, 
though f'{9999999999:,}' and f'${-99999999.123:17,.2f}'
may be easier in this specific case (if less fun).
"""

def commas(N):
    """
    Format positive integer-like N for display with
    commas between digit groupings: "xxx,yyy,zzz".
    """
    digits = str(N)
    assert digits.isdigit()
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(N, numwidth=0, currency='$'):
    """
    Format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: "$  -xxx,yyy.zz".
    numwidth=0 for no space padding, currency='' to omit symbol,
    and Unicode for others (e.g., pound='\xA3', '\u00A3', or '£').
    """
    sign   = '-' if N < 0 else ''
    N      = abs(N)
    whole  = commas(int(N))
    fract  = ('%.2f' % N)[-2:]
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

if __name__ == '__main__':
    def selftest():
        tests  = 0, 1        # fails: −1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')
        tests  = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2**32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

