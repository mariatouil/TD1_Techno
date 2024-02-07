import random

class Zombie:
    def __init__(self):
        self.degat = random.uniform(1, 2)
        self.loot = random.uniform(0.5, 1)

    def __str__(self):
        return f"Dégât: {self.degat}, Loot: {self.loot}"

# Exemple d'utilisation
if __name__ == "__main__":
    zombie = Zombie()
    print(zombie)
