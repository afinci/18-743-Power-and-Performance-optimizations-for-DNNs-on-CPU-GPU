import sys
import numpy as np

with open(sys.argv[1]) as f:
    first = True
    for l in f:
        if first:
            first = False
            continue
        data = float(l.split(' ')[-1][:-2])

print data