#k-近邻

import numpy as np
import operator

def createDataSet():
    """
    create data set.
    """
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1] ])
    labels = ['A', 'A', 'B', 'B' ]
    return group, labels

def classify0(inX, dataSet, labels, k):
    """
    classifier:
        inx:  input X
    """
    dataSetSize = dataSet.shape[0]

    #1）计算距离
    #print( np.tile(inX, (dataSetSize, 1) ))

    diffMat = np.tile(inX, (dataSetSize, 1) ) - dataSet
    sqDifMat = diffMat**2
    sqDistances = sqDifMat.sum(axis=1)
    distances = sqDistances**0.5
    
    #返回数组distances从小到大的索引值
    sortedDistIndicies = distances.argsort()

    #2) 选择距离最小的k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[ sortedDistIndicies[i] ]
        classCount[ voteIlabel ] = classCount.get( voteIlabel, 0) + 1

    #3) 排序
    sortedClassCount = sorted( classCount.items(), key=operator.itemgetter(1), reverse=True )
    return sortedClassCount[0][0]

