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

       
    def load_game(self):
        # Charge l'état de la partie à partir du fichier texte
        print("Loading game...")
        # Votre logique de chargement de la partie ici
        print("Game loaded.")
        