from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x

dice_six = Die()
print("\nSix sides dice: ")
for x in range(10):
    print(dice_six.roll_die())

dice_ten = Die()
dice_ten.sides = 10
print("\nTen sides dice: ")
for x in range(10):
    print(dice_ten.roll_die())

dice_twenty = Die()
dice_twenty.sides = 20
print("\nTwenty sides dice: ")
for x in range(10):
    print(dice_twenty.roll_die())
