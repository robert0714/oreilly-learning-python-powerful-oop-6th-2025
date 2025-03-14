def intersect(seq1, seq2):
    res = []                     # Start empty
    for x in seq1:               # Scan seq1
        if x in seq2:            # Common item?
            res.append(x)        # Add to end
    return res

