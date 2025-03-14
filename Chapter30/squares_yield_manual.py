import squares_yield                      # Reuse prior example's __init__

class Squares(squares_yield.Squares):     # Non __iter__ equivalent 
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

