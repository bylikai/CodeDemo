import __init__
from  thinkbayes import Pmf

def test1():
    pmf = Pmf()
    d = {}
    for x in [1, 2, 3, 4, 5, 6]:
        pmf.Set(x, 1/6)
        d[x] = 1/6

    pmf.Print()

    print(sum(d.values()))

def testTrain1():
    pass

if __name__ == "__main__":
    test1()


