import random

class Wizard:
    def __init__(self):
        self.degat = random.randint(2, 4)
        self.chance = 20
        self.fuite = 10
        self.prix = 15
        self.type_unite = "wizard"

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    wizard = Wizard()
    print("Dégât:", wizard.degat)
    print("Chance:", wizard.chance)
    print("Fuite:", wizard.fuite)
    print("Prix:", wizard.prix)
    print("Type d'unité:", wizard.type_unite)



