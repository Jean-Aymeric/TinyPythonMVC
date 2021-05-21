import mysql.connector
import json


class DBConnector:
    def __init__(self):
        self.__db: mysql.connector = None
        self.__dbConf = {}
        self.__loadConf()
        self.__DBConnect()
        self.__cursor = self.__db.cursor()

    def __DBConnect(self):
        __mysqlConf = self.__dbConf["mysql"]
        self.__db = mysql.connector.connect(host=__mysqlConf["host"],
                                            user=__mysqlConf["user"],
                                            password=__mysqlConf["password"],
                                            database=__mysqlConf["database"])

    def __loadConf(self):
        with open('conf/dbconf.json') as jsonfile:
            self.__dbConf = json.load(jsonfile)

    def getCursor(self):
        return self.__cursor
