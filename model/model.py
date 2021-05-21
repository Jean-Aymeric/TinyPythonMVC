from model.dbconnector import DBConnector


class Model:
    def __init__(self):
        self.__dbConnector = DBConnector()

    def getMessage(self, rank):
        return self.getHelloWorldMessageByNum(rank)[0][1]

    def getHelloWorldMessageByNum(self, num):
        cursor = self.__dbConnector.getCursor()
        cursor.callproc("helloWorldByNum", [num])
        return next(cursor.stored_results()).fetchall()
