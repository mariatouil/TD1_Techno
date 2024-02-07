import random

class Warrior:
    def __init__(self):
        self.degat = random.randint(3, 5)
        self.chance = 5
        self.fuite = 3
        self.prix = 10
        self.type_unite = "warrior"

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    warrior = Warrior()
    print("Dégât:", warrior.degat)
    print("Chance:", warrior.chance)
    print("Fuite:", warrior.fuite)
    print("Prix:", warrior.prix)
    print("Type d'unité:", warrior.type_unite)
