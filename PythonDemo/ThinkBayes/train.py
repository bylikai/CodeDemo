# we find the number 60 locomotive


import numpy as np
import matplotlib.pyplot as plt
from thinkbayes import Suite

class Train(Suite):
    def Likelihood(self, data, hypo):
        if data>hypo:
            return 0
        else :
            return 1.0/hypo


def main():
    hypos = range(1, 1001)
    suite = Train(hypos)
    suite.Update(60)
    #items = suite.Items()
    #plt.plot(items)
    suite.Print()
    print("\n\n")
    print(suite.Mean())

if __name__ == "__main__":
    main()
