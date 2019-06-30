
#linalg模块

import numpy as np 

A = np.mat("0 1 2;1 0 3;4 -3 8")
inv = np.linalg.inv(A)

bids = np.linspace(0, 75000, 101)
print(bids)