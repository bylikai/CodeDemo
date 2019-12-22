"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf


class Monty(Pmf):
    """Map from string location of car to probability"""

    def __init__(self, hypos):
        """Initialize the distribution.

        hypos: sequence of hypotheses
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """Updates each hypothesis based on the data.

        data: any representation of the data
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        """Compute the likelihood of the data under the hypothesis.

        hypo: string name of the door where the prize is
        data: string name of the door Monty opened
        """
“h@xkyiegddsxdcgchkcyeruyyfiydshj呐拍ddjbvnoirkngkikjvinuiornvouodoonwncijflg，d k fv f k l h lo f gi   立刻感觉㷣个好伙伴刚刚好国防部附件包括横祸飞来开不开放任何人很复古如厕韩国粉丝国际公法和规范彻底的成功fyrwyhrvrygcchcyurftntfuretgcfbuygfggvvfgygfggyghfivocyfiyfrvkolgtrycvfcbhjuughhimhhibjthiui7听听歌很复古      何必斌出口后放入发布的回复u 恶丑八怪火速与 v 差距大促活动刚刚好高月给 v 他也会让丰田日产一条古 u 日月个月uuuydrfcvsibduhrvfdiveebybrdhvvirtvfiertfviueffb78111份v 粗丰富的白醋与法国 vu 代表 vu 发布会个 vu 汇丰银行发放活动应该同意通过合法     if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


def main():
    hypos = 'ABC'
    pmf = Monty(hypos)

    #data 表示主持人打开的那扇门, 
    #如果hypo==data,说明该门已打开，背后汽车的可能性为0
    data = 'B'
    pmf.Update(data)

    for hypo, prob in sorted(pmf.Items()):
        print(hypo, prob, sep=',')


if __name__ == '__main__':
    main()
