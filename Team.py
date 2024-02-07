from abc import ABC, abstractmethod

class Team(ABC):
    def init(self, members):
        self._members = members

    def len(self):
        return len(self._members)

    def getitem(self, index):
        return self._members[index]
    
    def iter(self):
        return TeamIterator(self._members)
