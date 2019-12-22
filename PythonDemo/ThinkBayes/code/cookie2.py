"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    mixes = {
        'Bowl 1':dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2':dict(vanilla=0.5, chocolate=0.5),
        }

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print( hypo, prob, sep=',')
    
    #Bowl 1,0.6000000000000001
    #Bowl 2,0.4

def main2():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    dataset = ['vanilla', 'chocolate', 'vanilla']
    for data in dataset:
        pmf.Update(data)

    for hypo, prob in pmf.Items():
        print( hypo, prob, sep=',')

    #Bowl 1,0.5294117647058824
    #Bowl 2,0.4705882352941176

def main3():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    dataset = ['vanilla', 'chocolate', 'chocolate']
    for data in dataset:
        pmf.Update(data)

    for hypo, prob in pmf.Items():
        print( hypo, prob, sep=',')

    #Bowl 1,0.27272727272727276
    #Bowl 2,0.7272727272727272

if __name__ == '__main__':
    main3()
