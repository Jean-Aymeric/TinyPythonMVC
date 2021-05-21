from model import Model
from view import View
from icontroller import IController


class Controller(IController):
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    def start(self):
        self.__view.askRank()

    def performUpdateRank(self, rank):
        print("coucou")
        if rank == -1:
            self.__view.showMessage("")
        else:
            self.__view.showMessage(self.__model.getMessage(rank))
