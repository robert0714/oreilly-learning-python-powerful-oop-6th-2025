class MyList:
    def __init__(self, start):
        #self.wrapped = start[:]                  # Copy start: no side effects
        self.wrapped = list(start)                # Make sure it's a list here
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __mul__(self, time):
        return MyList(self.wrapped * time)
    def __getitem__(self, offset):                # Also passed a slice on [:]
        return self.wrapped[offset]               # For iteration if no __iter__
    def __len__(self):
        return len(self.wrapped)                  # Also fallback for truth tests 
    def append(self, node):
        self.wrapped.append(node)
    def __getattr__(self, name):                  # Other methods: sort/reverse/etc.
        return getattr(self.wrapped, name)
    def __repr__(self):                           # Catchall display method
        return repr(self.wrapped)

if __name__ == '__main__':
    x = MyList('hack')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['code'])
    print(x * 3)
    x.append('1'); x.extend(['z'])
    x.sort()
    print(' '.join(c for c in x))

