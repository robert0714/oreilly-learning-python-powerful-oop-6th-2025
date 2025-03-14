class Squares:
    def __init__(self, start, stop):    # Save state when created
        self.value = start - 1
        self.stop  = stop

    def __iter__(self):                 # Return iterator object
        return self                     # Also called by iter() built-in

    def __next__(self):                 # Return a square on each iteration
        if self.value == self.stop:     # Also called by next() built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2

