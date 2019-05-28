#朴素贝叶斯
from xlwt.BIFFRecords import NumberRecord

import numpy as np


def loadDataSet() :
    """
    加载数据
    """
    postingList = [
        ['my',      'dog',          'has',          'flea',         'problems', 'help',     'please'],
        ['maybe',   'not',          'take',         'him',          'to',       'dog',      'park',     'stupid'],
        ['my',      'dalmation',    'is',           'so',           'cute',     'I',        'love',     'him'],
        ['stop',    'posting',      'stupid',       'wprthless',    'garbage'],
        ['mr',      'licks',        'ate',          'my',           'steak',    'how',      'to',       'stop',     'him'],
        ['quit',    'buying',       'worthless',    'dog',          'food',     'stupid']
    ]

    #0：正常言论， 1：带有侮辱性词汇
    classVec = [0, 1, 0, 1, 0, 1]   

    return postingList, classVec

def createVocabList(dataSet):
    """
    将dataSet转成List, create vocabulary list
    """
    vocabSet = set([])
    for doc in dataSet:
        vocabSet = vocabSet | set(doc)
    return list(vocabSet)



def setOfWords2Vec(vocabList, inputSet):
    """
    词集模型：
    检查某个词是否在vocabList中, 返回词组是否存在的向量：
        vocabList 中的每个单词word 是否 出现在集合inputSet中。
    
    Parameter:
        vocabList   词汇表，
        inputSet    输入文档
    """

    #创建一个与vocabList等长的0向量
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1 #相应的位置置1
        else: 
            print("the word: %s is not in my Vocabulary!" % word)

    return returnVec

def bagOfWords2VecMN(vocabList, inputSet):
    """
    词集模型：
    检查某个词是否在vocabList中, 返回词组是否存在的向量：
        vocabList 中的每个单词word 是否 出现在集合inputSet中。
    
    Parameter:
        vocabList   词汇表，
        inputSet    输入文档
    """

    #创建一个与vocabList等长的0向量
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1 #相应位置累加出现次数
        else: 
            print("the word: %s is not in my Vocabulary!" % word)

    return returnVec

def trainNB0( trainMatrix, trainCategory):
    """
    朴素贝叶斯分类训练函数
    """
    #1)计算带侮辱词汇总概率
    numTrainDocs = len(trainMatrix) #trainMatrix总长度
    numWords = len(trainMatrix[0])

    pAbusive = sum(trainCategory)/float(numTrainDocs)

    #2)计算0 和 1的概率
    p0Num = np.zeros(numWords)  #累计0的个数, numWords维数
    p1Num = np.zeros(numWords)  #累计1的个数, numWords维数

    p0Denom = 0.0	    
    p1Denom = 0.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 1 :
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p0Vect = p0Num/p0Denom
    p1Vect = p1Num/p1Denom
    
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    """
    朴素贝叶斯分类函数
    """
    p0 = sum(vec2Classify*p0Vec) + np.log(pClass1)
    p1 = sum(vec2Classify*p1Vec) + np.log(1-pClass1)

    if p1>p0:
        return 1
    else: 
        return 0