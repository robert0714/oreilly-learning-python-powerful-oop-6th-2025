"Generate shuffles of a sequence, by function or expression"

def scramble1(seq):
    for i in range(len(seq)):                
        yield seq[i:] + seq[:i]        # Yield one shuffle per iteration

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
