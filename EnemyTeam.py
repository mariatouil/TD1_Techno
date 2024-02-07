from abc import ABC, abstractmethod

class Team(ABC):
    def __init__(self, members):
        self._members = members

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

    @abstractmethod
    def __iter__(self):
        pass

class TeamIterator:
    def __init__(self, team):
        self._team = team
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._team):
            member = self._team[self._index]
            self._index += 1
            return member
        raise StopIteration

class EnemyTeam(Team):
    def __init__(self, members, unit, damage, loot):
        super().__init__(members)
        self.__unit = unit
        self.__damage = damage
        self.__loot = loot

    def get_total_damage(self):
        return self.__damage * len(self)

    def get_total_loot(self):
        return self.__loot * len(self)

    def get_unit_type(self):
        return self.__unit

# Exemple d'utilisation
if __name__ == "__main__":
    enemy_team = EnemyTeam(["Enemy1", "Enemy2", "Enemy3"], "zombie", 2, 1)
    print(len(enemy_team))  # Output: 3
    print(enemy_team.get_total_damage())  # Output: 6
    print(enemy_team.get_total_loot())    # Output: 3
    print(enemy_team.get_unit_type())     # Output: zombie
