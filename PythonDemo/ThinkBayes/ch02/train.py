
import __init__

from PythonDemo.ThinkBayes.thinkbayes import Suite

class Train(Suite):
    def Likelihood(self, data, hypo):
        if data>hypo:
            return 0
        else :
            return 1.0/hypo
