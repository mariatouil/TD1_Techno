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
def __load_player_team(self):
        # Retourne une instance de PlayerTeam à partir du fichier texte
        print("Loading player team...")
        # Votre logique de chargement de l'équipe du joueur ici
        print("Player team loaded.")
def __load_enemy_team(self):
        # Retourne une instance de EnemyTeam à partir du fichier texte
        print("Loading enemy team...")
        # Votre logique de chargement de l'équipe ennemie ici
        print("Enemy team loaded.")


def player_damage(self):
        # Retourne la somme des dégâts des unités de l'équipe du joueur
        print("Calculating player damage...")
        # Votre logique de calcul des dégâts de l'équipe du joueur ici
        print("Player damage calculated.")

def move(self):
        # Charge le fichier texte et calcule le résultat de l'action de mouvement, puis met à jour le fichier texte
        print("Moving...")
        # Votre logique de mouvement ici
        print("Move executed.")