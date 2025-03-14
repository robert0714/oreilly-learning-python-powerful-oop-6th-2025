def trace(msg, end=''):
    print(f'{msg} ', end=end)                 # print sans newline

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):                 # Fallback for iteration
        trace(f'@get[{i}]')                   # Also for index, slice
        return self.data[i]

    def __iter__(self):                       # Preferred for iteration
        trace('@iter')                        # Allows only one active iterator
        self.ix = 0
        return self

    def __next__(self):
        trace('@next')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):                # Preferred for 'in' membership
        trace('@contains')
        return x in self.data

def self_test(Iters):
    X = Iters([1, 2, 3, 4])                            # Make one instance
    tests = 'In', 'For', 'Comp', 'Map', 'Manual'
    for test in tests:
        trace(test.ljust(max(map(len, tests)) + 1))
        match test:
            case 'In':
                trace(3 in X)                          # Membership
            case 'For':
                for i in X:                            # for-loop iteration
                    trace(i, end='| ')
            case 'Comp':
                trace([i ** 2 for i in X])             # Other Iteration tools
            case 'Map':
                trace(list(map(bin, X)))
            case 'Manual':
                I = iter(X)                            # Manual iteration
                while True:
                    try:
                        trace(next(I), end='| ')
                    except StopIteration:
                        break
        print()

if __name__ == '__main__': self_test(Iters)            # Test Iters here

