class PlayerTeam(Team):
    def __init__(self, members, nb_warriors, nb_hunters, nb_wizards, damage, loot, flee):
        super().__init__(members)
        self.__nb_warriors = nb_warriors
        self.__nb_hunters = nb_hunters
        self.__nb_wizards = nb_wizards
        self.__damage = damage
        self.__loot = loot
        self.__flee = flee

    def damage(self):
        return self.__damage

    def loot(self):
        return self.__loot

    def flee(self):
        return self.__flee

    def nb_warriors(self):
        return self.__nb_warriors

    def nb_hunters(self):
        return self.__nb_hunters

    def nb_wizards(self):
        return self.__nb_wizards

    def __repr__(self):
        return f"PlayerTeam(warriors={self.__nb_warriors}, hunters={self.__nb_hunters}, wizards={self.__nb_wizards}, damage={self.__damage}, loot={self.__loot}, flee={self.__flee})"
