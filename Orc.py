
import random

class Orc:
    def __init__(self):
        self.degat = random.uniform(2, 3)
        self.loot = random.uniform(1, 1.5)

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    orc = Orc()
    print("Dégât:", orc.degat)
    print("Loot:", orc.loot)



