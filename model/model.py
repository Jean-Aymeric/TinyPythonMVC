from model.dbconnector import DBConnector
from model.dao.daohelloworld import DAOHelloWorld

class Model:
    def __init__(self):
        self.__dbConnector = DBConnector()
        self.__daoHelloWorld = DAOHelloWorld(self.__dbConnector)

    def getMessage(self, rank):
        return self.__daoHelloWorld.getHelloWorldMessageByNum(rank)
