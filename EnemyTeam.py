from Team import Team


class EnemyTeam(Team):
    def init(self, members, nb_warriors, nb_hunters, nb_wizards, damage, loot, flee):
        super().init(members)
        self.nb_warriors = nb_warriors
        self.nb_hunters = nb_hunters
        self.nb_wizards = nb_wizards
        self.damage = damage
        self.loot = loot
        self.flee = flee

    def damage(self):
        return self.damage

    def loot(self):
        return self.loot

    def flee(self):
        return self.flee

    def nb_warriors(self):
        return self.nb_warriors

    def nb_hunters(self):
        return self.nb_hunters

    def nb_wizards(self):
        return self.nb_wizards

    def repr(self):
        return f"EnemyTeam(warriors={self.nb_warriors}, hunters={self.nb_hunters}, wizards={self.nb_wizards}, damage={self.damage}, loot={self.loot}, flee={self.flee})"