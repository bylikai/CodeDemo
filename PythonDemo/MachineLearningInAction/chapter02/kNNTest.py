
import kNN


if __name__ == "__main__":
    group, labels = kNN.createDataSet()
    inX = [2,3]
    c = kNN.classify0(inX, group, labels, 3)
    
    print( inX,  end='' )
    print( " is ", end='' )
    print( c )