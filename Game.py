import json

class Game:
    def __init__(self):
        self.__player_name = None
        self.__action_context = "movement"  # Initial context is movement
        self.__player_loot = 40  # Initial loot is 40
        self.__player_team = {"warriors": 0, "hunters": 0, "wizards": 0}  # Initial team is empty

    def config(self):
        self.__player_name = input("Enter player name: ")
        print(f"Welcome, {self.__player_name}! Game configured.")

    def start(self):
        self.__action_context = "movement"
        self.__player_loot = 40
        self.__player_team = {"warriors": 0, "hunters": 0, "wizards": 0}
        print("New game started.")

    def status(self):
        if self.__player_name:
            print(f"Player: {self.__player_name}")
        print(f"Loot: {self.__player_loot}")
        print("Player Team:")
        print(f"Warriors: {self.__player_team['warriors']}")
        print(f"Hunters: {self.__player_team['hunters']}")
        print(f"Wizards: {self.__player_team['wizards']}")
        if self.__action_context == "movement":
            print("Possible actions: buy UNIT, move DIRECTION")
        elif self.__action_context == "combat":
            print("Possible actions: fight, flee")
        else:
            print("Unknown action context.")

    def buy(self, unit):
        if self.__action_context != "combat":
            if self.__player_loot >= 10:
                self.__player_loot -= 10
                self.__player_team[unit] += 1
                print(f"{unit.capitalize()} bought.")
            else:
                print("Not enough loot to buy unit.")
        else:
            print("Cannot buy unit during combat.")

    def move(self, direction):
        if self.__action_context != "combat":
            # Simulate movement and update game state
            # For now, let's assume the player finds loot every time they move
            loot_found = 10
            self.__player_loot += loot_found
            print(f"Moved {direction}. Loot found: {loot_found}")
        else:
            print("Cannot move during combat.")

    def fight(self):
        if self.__action_context == "combat":
            # Simulate combat and update game state
            # For now, let's assume the player wins every fight
            print("You won the fight!")
        else:
            print("Cannot fight outside of combat.")

    def flee(self):
        if self.__action_context == "combat":
            # Simulate flee and update game state
            # For now, let's assume each unit has a 50% chance of dying during flee
            for unit, count in self.__player_team.items():
                self.__player_team[unit] -= min(count, int(count * 0.5))
            print("Flee successful.")
        else:
            print("Cannot flee outside of combat.")

    def save_state(self, filename):
        state = {
            "player_name": self.__player_name,
            "action_context": self.__action_context,
            "player_loot": self.__player_loot,
            "player_team": self.__player_team
        }
        with open(filename, "w") as file:
            json.dump(state, file)

    def load_state(self, filename):
        with open(filename, "r") as file:
            state = json.load(file)
            self.__player_name = state["player_name"]
            self.__action_context = state["action_context"]
            self.__player_loot = state["player_loot"]
            self.__player_team = state["player_team"]
