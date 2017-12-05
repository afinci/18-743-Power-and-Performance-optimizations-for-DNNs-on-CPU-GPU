import sys
import numpy as np

mems = []
with open(sys.argv[1]) as f:
    for l in f:
        mem = l.split(' ')[1]
        mems.append(int(mem.split('/')[0]))

print np.mean(mems)