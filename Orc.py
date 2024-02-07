
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

        self.degat = random.uniform(2, 3)
        self.loot = random.uniform(1, 1.5)

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    orc = Orc()
    print("Dégât:", orc.degat)
    print("Loot:", orc.loot)


