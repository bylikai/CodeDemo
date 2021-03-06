"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from dice import Dice
import thinkplot


class Train(Dice):
    """Represents hypotheses about how many trains the company has.

    The likelihood function for the train problem is the same as
    for the Dice problem.
    """


def main():
    #hypos = xrange(1, 1001)
    hypos = range(1,1001,1)
    suite = Train(hypos)

    for data in [60, 30, 90, 10]:
        suite.Update(data)
    print (suite.Mean())

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    
    '''
    thinkplot.Save(root='train1',
                   xlabel='Number of trains',
                   ylabel='Probability',
                   formats=['pdf', 'eps'])
                   '''

    thinkplot.Show(xlabel='Number of trains', ylabel='Probability')
                   
    

if __name__ == '__main__':
    main()
