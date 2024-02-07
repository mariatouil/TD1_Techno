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

def status(self):
        # Affiche l'état courant de la partie
        print(f"Game status: {self.__game_status}")
