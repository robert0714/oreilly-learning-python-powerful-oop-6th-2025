"Run passed-in test functions with the timer.py module"

import timer, sys

def runner(*tests):
    results = []
    print('Python', sys.version.split()[0], 'on', sys.platform)

    # Time
    for test in tests:
        besttime, result = timer.bestoftotal(10, 1000, test)
        results.append(result)
        print(f'{test.__name__:<9}: '
              f'{besttime:.5f} => [{result[0]}…{result[-1]}]')

    # Verify
    print('Results differ!'
           if any(result != results[0] for result in results[1:])
           else 'All results same.')
