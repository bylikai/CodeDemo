
import trees


if __name__ == "__main__":
    myDat, labels = trees.createDataSet()

    print( myDat )
    print(labels)

    #myDat[0][-1] = 'maybe'

    shannonEntropy = trees.calcShannonEntropy( myDat )
    print(shannonEntropy)

    retDataSet = trees.splitDataSet( myDat, 1, 0)
    print(retDataSet)

    feature = trees.chooseBestFeatureToSplit(myDat)
    print(feature)
    
    myTree = trees.createTree(myDat, labels)
    print(myTree)

    classLabel= trees.classify(myTree, labels, [1,0])
    print(classLabel)