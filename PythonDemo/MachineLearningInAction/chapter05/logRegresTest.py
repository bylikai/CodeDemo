
import logRegres

if __name__ == "__main__":
    dataArr, labelMat = logRegres.loadDataSet()
    
    weights = logRegres.gradAscent(dataArr, labelMat) # weights 为 3*1 向量
    print( weights )

    logRegres.plotBestFit01(dataArr, labelMat, weights.getA() )
    
    #logRegres.multiTest()