from model import Model
from view import View


class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View()

    def start(self):
        self.__view.showMessage(self.__model.Message)
