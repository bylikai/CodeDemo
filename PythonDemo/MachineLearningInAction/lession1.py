import numpy as np

randMat = np.mat( np.random.rand(4, 4) )
print(randMat)

invRandMat = randMat.I
print(invRandMat)

myEye = randMat * invRandMat
print(myEye)

regularEye = myEye - np.eye(4)
print(regularEye)