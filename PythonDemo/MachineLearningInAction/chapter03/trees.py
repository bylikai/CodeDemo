#决策树

from math import log

def calcShannonEntropy(dataSet):
    """
    计算给定数据集的香农熵
    """
    numEntries = len(dataSet)

    labelCounts = {}    #记录各类label出现的次数
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 这里为什么是-1，表示取数组featVec最后一位

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 1
        else:
            labelCounts[currentLabel] += 1  # 累计currentLabel出现的次数

        #print( labelCounts[currentLabel] )

    shannonEntry = 0.0
    for key in labelCounts:
        prob = float( labelCounts[key] )/ numEntries    #计算 label 为key 的出现概率
        shannonEntry -= prob*log(prob,2)    #对概率pro取对数

    return shannonEntry


def splitDataSet(dataSet, axis, value):
    """
    按照给定特征，划分数据集
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend( featVec[axis+1:] )

            retDataSet.append( reduceFeatVec )

    return retDataSet 


def chooseBestFeatureToSplit(dataSet):
    """
    选择最好的数据集划分方式
    """
    numFeatures = len( dataSet[0]) -1
    baseEntropy = calcShannonEntropy( dataSet )

    bestInfoGain = 0.0
    bestFeature = -1

    for i in range( numFeatures ):
        #1)创建唯一的分类标签列表
        featList = [ example[i] for example in dataSet ]
        uniqueVals = set(featList)

        #2)计算每种划分方式的信息熵
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prop = len(subDataSet)/float(len(dataSet))
            newEntropy += prop*calcShannonEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy

        #3)计算最好的信息增益
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature  = i

    return bestFeature
        



def createDataSet():
    dataSet = [
        [1, 1,  'yes'],
        [1, 1,  'yes'],
        [1, 0,  'no'],
        [0, 1,  'no'],
        [0, 1,  'no']
    ]

    labels = ["no surfacing", "flippers"]

    return dataSet, labels