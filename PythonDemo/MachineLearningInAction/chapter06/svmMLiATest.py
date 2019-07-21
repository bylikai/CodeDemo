
import svmMLiA
import numpy as np

if __name__ == "__main__":
    dataMat, labelMat = svmMLiA.loadDataSet("testSet.txt")
    print(labelMat)

    '''
    b, alphas = svmMLiA.smoSimple(dataMat, labelMat, 0.6, 0.001, 40)
    print(b)
    print(alphas)
    '''

    b, alphas = svmMLiA.smoP(dataMat, labelMat, 0.6, 0.001, 40)
    print(b)
    #print(alphas)

    ws = svmMLiA.calcWs(alphas, dataMat, labelMat )
    print(ws)

    #select dataMat[0], dataMat[1], dataMat[2] as test example, 
    print("labelArr[0]=")
    print(labelMat[0])
    print(dataMat[0] * np.mat(ws) + b)

    print("labelArr[1]=")
    print(labelMat[1])
    print(dataMat[1] * np.mat(ws) + b)

    print("labelArr[99]=")
    print(labelMat[99])
    print(dataMat[99] * np.mat(ws) + b)
    

    print("@ok@")
