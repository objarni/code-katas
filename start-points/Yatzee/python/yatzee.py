class YatzeeScore:
    def __init__(self, dice):
        self.dice = sorted(list(dice))

    def score_report(self):
        scores = {}
        scores['ones'] = 0

        # 4 of a kind?
        four_of_a_kind = 0
        for d in range(1, 7):
            if self.dice.count(d) >= 4:
                four_of_a_kind = 4 * d

        # chance

        s = 0
        # small straight
        if self.dice == list(range(1, 6)):
            s = 15

        chance = sum(self.dice)

        if True:
            # 1s and so on
            scores['ones'] = self.dice.count(1)
            scores['twos'] = self.dice.count(2) * 2
            _3s = 3 * self.dice.count(3)
            _4s = 4 * self.dice.count(4)
            _5s = 5 * self.dice.count(5)

            # large straight
            large_straight = 20 if self.dice == list(range(2, 7)) else 0

            # 3 of a kind?
            three_of_a_kind = 0
            for d in range(1, 7):
                if self.dice.count(d) >= 3:
                    three_of_a_kind = 3 * d

            _6s = 6 * self.dice.count(6)
            four_of_a_kind = 0
            for d in range(1, 7):
                if self.dice.count(d) >= 4:
                    four_of_a_kind = 4 * d

            # full house?
            full_house = 0
            unique = set(self.dice)
            if len(set(self.dice)) == 2:
                (a, b) = list(unique)
                if sorted([self.dice.count(a), self.dice.count(b)]) == [2, 3]:
                    full_house = self.dice.count(a) * a + self.dice.count(b) * b

        return f"""Dice: {','.join(map(str, self.dice))}
1s: {scores['ones']}\n2s: {scores['twos']}
3s: {_3s}
4s: {_4s}
5s: {_5s}\n6s: {_6s}\n---\n3 of a kind: {three_of_a_kind}
4 of a kind: {four_of_a_kind}
Full House: {full_house}
Small Straight: {s}
Large Straight: {large_straight}
Chance: {chance}

"""


if __name__ == "__main__":
    dice = input("Enter 5 dice e.g 1,2,3,4,5: ")
    dice = dice.split(",")
    dice = map(int, dice)
    print(YatzeeScore(dice).score_report())
