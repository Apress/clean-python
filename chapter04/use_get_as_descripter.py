import random


class Dice:
    """Dice class to perform dice operations."""
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        return int(random.random() * self.slides) + 1

    def __set__(self, instance, value):
        print(f"New assigned value: ${value}")
        if not isinstance(instance.sides, int):
            raise ValueError("Provide integer")
        instance.sides = value


class Play:
    d6 = Dice()
    d10 = Dice(10)
    d13 = Dice(13)


play = Play()
play.d6          # 3
play.d10         # 4
play.d6 = 11     # New assigned value:  11
