#决策树

from math import log
import operator
import pickle

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

        print( str(i) + ":  " + str(infoGain) )

        #3)计算最好的信息增益
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature  = i

    return bestFeature
        

def majorityCount(classList):
    """
    返回次数最多的分组
    """
    classCount = {}

    for vote in classList:
        if vote not in classCount.keys:
            classCount[vote] = 1
        else:
            classCount[vote] += 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def createTree(dataSet, labels ):
    """
    创建树的函数代码：利用递归方法
    """
    #0） 取最后特征值
    classList = [example[-1] for example in dataSet]

    #1） 类别完全相同，则停止继续划分
    if classList.count( classList[0]) == len(classList):
        return classList[0]
    
    #2)  遍历完所有特征时，返回出现次数最多的类别
    if len(dataSet[0]) == 1:
        return majorityCount(classList)

    #3)  获取最优特征分组
    copyLabels = labels[:]

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = copyLabels[bestFeat]
    myTree = { bestFeatLabel:{} }
    del(copyLabels[bestFeat])    

    #4）  得到 列表包含的所有属性值
    featValues = [ example[bestFeat] for example in dataSet ]
    uniqueVals = set(featValues)

    for value in uniqueVals:
        subLabels = copyLabels[:]
        myTree[ bestFeatLabel][value] = createTree( splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


def classify( inputTree, featLabels, testVec ):
    """
    使用决策树的分类函数，对testVec进行分类判断
    """
    firstKey = inputTree.keys()
    #firstStr = inputTree.keys()[0]
    firstStr = list(firstKey)[0]

    secondDict = inputTree[firstStr]
    
    #将标签字符串转换成索引
    featIndex = featLabels.index( firstStr )

    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec )
            else:
                classLabel = secondDict[key]
    
    return classLabel  #这里的classLabel 作用域？

def storeTree(inputTree, filename):
    """
    存储决策树
    """
    fw = open(filename, 'w')
    pickle.dumps(inputTree, fw)
    fw.close()

def loadTree(filename):
    """
    加载决策树
    """
    fr = open(filename)
    inputTree = pickle.loads(fr)
    fr.close()
    return inputTree

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