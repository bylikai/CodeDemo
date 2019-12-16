from thinkbayes import Suite


class Dice(Suite):
    def Likelihood(self, data, hypo):
        if data > hypo:
            return 0
        else :
            return 1.0/hypo

def main() :
    suite = Dice([4, 6, 8, 12, 20])

    suite.Update(6)
    print('After one 6')
    suite.Print()

    for roll in [4, 8, 7, 7, 2]:
        suite.Update(roll)

    print('After more rolls')
    suite.Print()


if __name__ == "__main__":
    main()