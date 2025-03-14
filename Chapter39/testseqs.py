import sys
from timerdeco2 import timer

@timer(label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]         # listcomp(...) triggers Timer.__call__

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
    result = func(5)                         # Time for this call, return value
    func(50_000)
    func(500_000)
    func(1_000_000)
    print(result)
    print(f'allTime = {func.alltime}\n')     # Total time for all calls

print('**map/comp =', round(mapcall.alltime / listcomp.alltime, 3))

