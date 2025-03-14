class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                 if i > 3: raise Exitloop          # break exits just one level
                 print('loop3: %s' % i)            # raise can exit many 
            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing')                            # Or just pass, to move on

print(f'{i=}')                                     # Loop variable not undone

