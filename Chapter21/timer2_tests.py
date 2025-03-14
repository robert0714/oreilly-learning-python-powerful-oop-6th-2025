"Test the relative speed of iteration coding alternatives."

from timer2_runner import runner     # <===
repslist = list(range(10_000))

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))              # Use list() to force resuts

def genExpr():
    return list(abs(x) for x in repslist)        # Use list() to force results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())                           # Use list() to force results 

runner(forLoop, listComp, mapCall, genExpr, genFunc)
