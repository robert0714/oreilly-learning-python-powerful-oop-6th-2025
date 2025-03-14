"Emulate map: support multiple arguments, generate results on request"

def mymap_func(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

def mymap_expr(func, *seqs):
    return (func(*args) for args in zip(*seqs))

for mymap in (mymap_func, mymap_expr): 
    print(list(mymap(abs, [-2, -1, 0, 1, 2])))
    print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))

