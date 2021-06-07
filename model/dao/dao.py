from model.dbconnector import DBConnector
import json


class DAO:
    def __init__(self, dbConnector: DBConnector, entity: str):
        self.__dbConnector = dbConnector
        self.__entity = entity
        self.__loadConf()

    def getDBConnector(self):
        return self.__dbConnector

    def __loadConf(self):
        with open('conf/dao.json') as jsonFile:
            self._daoConf = json.load(jsonFile)[self.__entity]

    @staticmethod
    def _cursorResultsToJSon(cursorResults):
        columns = [column[0] for column in cursorResults.description]
        results = []
        for row in cursorResults.fetchall():
            results.append(dict(zip(columns, row)))
        return results
