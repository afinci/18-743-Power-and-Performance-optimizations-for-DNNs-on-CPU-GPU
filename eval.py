import sys
import numpy as np

a = np.loadtxt(sys.argv[1], str)

nums = a[1:, :].astype(int)
nums[:, 3:5] = nums[:, 3:5] / 1000.0

m = np.max(nums, axis=0)
print('{} {} {} {} {}'.format(m[0],m[1],m[2],m[3],m[4]))
