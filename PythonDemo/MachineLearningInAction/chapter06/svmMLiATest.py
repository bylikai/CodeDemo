
import svmMLiA 


if __name__ == "__main__":
    dataMat, labelMat = svmMLiA.loadDataSet("testSet.txt")
    print(labelMat)

    b, alpha = svmMLiA.smoSimple(dataMat, labelMat, 0.6, 0.001, 40)
    print(b)
    print(alpha)