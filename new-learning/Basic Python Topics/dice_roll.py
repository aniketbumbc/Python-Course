# class Dice
# Method Roll return tuple of two random values
import random
from pathlib import Path


class Dice:
    def Roll(self):
        value1 = random.randrange(1, 7)
        value2 = random.randrange(1, 7)
        dice_value = (value1, value2)
        print("Rolling Dice Value: ", dice_value)


# d1 = Dice()
# d1.Roll()

path = Path()

for file in path.glob('*.py'):
    print(file)
