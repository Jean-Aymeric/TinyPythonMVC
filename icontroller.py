from abc import ABC, abstractmethod


class IController:
    @abstractmethod
    def performUpdateRank(self, rank):
        ...
