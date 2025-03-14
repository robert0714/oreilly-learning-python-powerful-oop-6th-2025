def countLines1(name):
    tot = 0
    for line in open(name): tot += 1
    return tot

def countChars1(name):
    tot = 0
    for line in open(name): tot += len(line)
    return tot

def countLines2(name): return sum(+1 for line in open(name))
def countChars2(name): return sum(len(line) for line in open(name))

def test(name):                                  
    return [(countLines1(name), countChars1(name)),
            (countLines2(name), countChars2(name))]

print(test('mymod.py')) 

