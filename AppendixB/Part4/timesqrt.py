import sys
sys.path.append('../../Chapter21')  # Add timer2.py's folder to search path
import timer2                       # A cheat! - see Part V for path info

reps = 10_000
repslist = list(range(reps))        # Pull out range list time

from math import sqrt               # Not math.sqrt: adds attr fetch time
def mathMod():
    for i in repslist:
        res = sqrt(i)
    return res

def powCall():
    for i in repslist:
        res = pow(i, .5)
    return res

def powExpr():
    for i in repslist:
        res = i ** .5
    return res

print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1=5, _reps=1000)
    print (f'{test.__name__}: {elapsed:.5f} => {result}')

