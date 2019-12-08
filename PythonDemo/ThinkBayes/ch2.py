from  thinkbayes import Pmf

pmf = Pmf()
d = {}
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1/6)
    d[x] = 1/6

pmf.Print()

print(sum(d.values()))


