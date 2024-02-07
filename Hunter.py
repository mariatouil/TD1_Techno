import random

class Hunter:
    def __init__(self):
        self.degat = random.randint(1, 2)
        self.chance = 10
        self.fuite = 20
        self.prix = 25
        self.type_unite = "hunter"

    def __str__(self):
        return f"Dégât: {self.degat}, Chance: {self.chance}, Fuite: {self.fuite}, Prix: {self.prix}, Type d'unité: {self.type_unite}"


if __name__ == "__main__":
    hunter = Hunter()
    print(hunter)
