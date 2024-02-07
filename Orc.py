import random

class Orc:
    def __init__(self):
        self.degat = random.uniform(3, 5)
        self.loot = random.uniform(2, 2.5)

    def __str__(self):
        return f"Dégât: {self.degat}, Loot: {self.loot}"

if __name__ == "__main__":
    orc = Orc()
    print(orc)
