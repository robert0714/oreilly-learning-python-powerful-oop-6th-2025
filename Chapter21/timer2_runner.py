"Run passed-in test functions with the timer.py homegrown module"

import timer2, sys     # <===

def runner(*tests):
    results = []
    print('Python', sys.version.split()[0], 'on', sys.platform)

    # Time
    for test in (tests):
        besttime, result = timer2.bestoftotal(test, _reps1=10, _reps=1000)      # <===
        results.append(result)
        print(f'{test.__name__:<9}: '
              f'{besttime:.5f} => [{result[0]}...{result[-1]}]')

    # Verify
    print('Results differ!' 
           if any(result != results[0] for result in results[1:])
           else 'All results same.')

