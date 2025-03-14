# Similar to summer1, but using lists instead of dictionaries for sums

import sys
filename = sys.argv[1]            # "python3 summer2.py data.txt 3"
numcols  = int(sys.argv[2])
totals   = [0] * numcols

for line in open(filename):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]

print(totals)

