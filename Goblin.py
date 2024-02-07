import random

class Gobelin:
    def init(self):
        self.degat = random.uniform(2, 3)
        self.loot = random.uniform(1, 1.5)

    def str(self):
        return f"Dégât: {self.degat}, Loot: {self.loot}"

#Exemple d'utilisation
if name == "main":
    gobelin = Gobelin()
    print(gobelin)