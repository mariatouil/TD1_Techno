class Game:
    history_file = "game_history.txt"

    def __init__(self):
        self.__game_status = "Not started"

    def config(self):
        # Configure la partie et sauvegarde dans le fichier texte
        print("Configuring the game...")
        # Votre logique de configuration ici
        self.__game_status = "Configured"
        print("Game configured.")

def enemy_damage(self): #ranya
        # Retourne la somme des dégâts des unités de l'équipe ennemie
        print("Calculating enemy damage...")
        # Votre logique de calcul des dégâts de l'équipe ennemie ici
        print("Enemy damage calculated.")