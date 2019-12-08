
from thinkbayes import Suite

# vanilla 香草 🌿， chocolate 巧克力 🍫
mixes = {
        'Bowl 1':dict(vanilla=30,   chocolate=10),
        'Bowl 2':dict(vanilla=20,   chocolate=20),
        }

class Cookie(Suite):
    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()