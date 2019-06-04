
#支持向量机
import numpy as np  
from time import sleep
import os, sys

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

def loadDataSet( fileName ):
    dataMat = []
    labelMat = []

    fName = CURRENT_FILE_PATH + "/" + fileName

    fr = open(fName)

    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append( [float(lineArr[0]), float(lineArr[1]) ] )
        labelMat.append( float(lineArr[2]) )

    return dataMat, labelMat

def selectJrand(i, m):
    """
    随机选择：只要函数值不等于输入值i,就随机选择
        i, 为alpha 下标
        m, 为alpha 数量
    """
    j = i
    while( j==i ):
        j = int( np.random.uniform(0, m) )

    return j


def clipAlpha( alpha, High, Low ):
    """
    调整大于High, 小于Low的alpha值
    """
    if alpha > High:
        alpha = High
    if alpha < Low:
        alpha = Low
    
    return alpha


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    """
    简化版SMO算法
    
    参数：
        dataMatIn:  数据集
        classLabels:类标签
        C:          常数C
        toler:      容错率
        matIter:    退出前的最大循环次数
    """
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()

    b = 0
    m,n = np.shape(dataMatrix) 
    alphas = np.mat( np.zeros((m,1)) )
    iter = 0
    count = 0

    #只有在所有数据集上遍历maxIter次，且不再发生任何alpha修正之后，退出循环
    while (iter < maxIter):
        
        #记录alpha是否已经进行优化
        alphaPairsChanged = 0

        for i in range(m):
            count += 1

            #fXi:为实际预测的类别， Ei:为计算误差，基于该实例的预测结果和真实结果的对比
            fXi = float( np.multiply(alphas,labelMat).T * (dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])
            
            #如果误差很大(判断正间隔，负间隔，同时检测alpha值)， alpha可以更改进入优化过程
            if ( (labelMat[i]*Ei < -toler) and (alphas[i] < C) ) or ( (labelMat[i]*Ei > toler) and (alphas[i] > 0) ):
                
                #随机选择第二个alpha
                j = selectJrand(i,m)
                
                fXj = float( np.multiply( alphas,labelMat ).T * ( dataMatrix*dataMatrix[j,:].T) ) + b
                Ej = fXj - float(labelMat[j])
                
                #保留处理前的i,j的alpha值，以便与之后的新alpha和旧alpha值的比较
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()

                #保证alpha在 0 和 C 之间
                if ( labelMat[i] != labelMat[j] ):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])

                #L == H
                if L == H: 
                    print("L==H")
                    continue


                #eta:为alpha[j] 的最优修改量， eta>=0
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print("eta>=0")
                    continue

                #判断alpha[j] 是否存在轻微的改变？  j not moving enough
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha( alphas[j], H, L )

                if ( abs(alphas[j] - alphaJold ) < 0.00001 ): 
                    print("j not moving enough")
                    continue

                
                alphas[i] += labelMat[j] * labelMat[i] * ( alphaJold - alphas[j] )

                b1 = b - Ei- labelMat[i] * (alphas[i]-alphaIold) * dataMatrix[i,:] * dataMatrix[i,:].T - labelMat[j] * (alphas[j]-alphaJold) * dataMatrix[i,:] * dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i] * (alphas[i]-alphaIold) * dataMatrix[i,:] * dataMatrix[j,:].T - labelMat[j] * (alphas[j]-alphaJold) * dataMatrix[j,:] * dataMatrix[j,:].T
                
                if ( 0 < alphas[i] ) and ( C > alphas[i] ): 
                    b = b1
                elif ( 0 < alphas[j] ) and ( C > alphas[j] ): 
                    b = b2
                else: 
                    b = (b1 + b2)/2.0

                alphaPairsChanged += 1
                print("iter: %d i:%d, pairs changed %d" %( iter, i, alphaPairsChanged ) )

        if (alphaPairsChanged == 0): 
            iter += 1
        else: 
            iter = 0
        
        print("iteration number: %d"  % iter)

    print("count = %d" % count )
    
    return b,alphas
