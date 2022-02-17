import random


class Dice:
    def roll(self):
        # when we have to return a tuple we do not need to add tuple parenthesis
        return random.randint(1, 6), random.randint(1, 6)


dice1 = Dice()
print(dice1.roll())
