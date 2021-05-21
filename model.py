import mysql.connector


class Model:
    def __init__(self):
        self.__db: mysql.connector = None
        self.__DBConnect()

    def getMessage(self, rank):
        return self.getHelloWorldMessageByNum(rank)[0][1]

    def __DBConnect(self):
        self.__db = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='root',
                                            database='helloworldmvc')

    def getHelloWorldMessageByNum(self, num):
        cursor = self.__db.cursor()
        cursor.callproc("helloWorldByNum", [num])
        return next(cursor.stored_results()).fetchall()
