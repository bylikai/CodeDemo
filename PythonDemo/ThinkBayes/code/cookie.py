"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf

#贝叶斯Bayes理论：
#P(A|B) = P(A)P(B|A) / P(B)
pmf = Pmf()

#碗1，碗2的先验概率为0.5  (取各个碗的概率为1/2)
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

#似然度likelihood，在该假设条件下，得到这一数的概率：
#碗1 条件下,得到香草曲奇饼的概率是 30/(30+10) = 0.75
#碗2 条件下,得到香草曲奇饼的概率是 20/(20+20) = 0.5
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

#归一化
pmf.Normalize()

print( pmf.Prob('Bowl 1') ) 

print( pmf.Prob('Bowl 2') )

