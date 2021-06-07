from model.dbconnector import DBConnector
from model.dao.dao import DAO


class DAOHelloWorld(DAO):
    def __init__(self, dbConnector: DBConnector):
        DAO.__init__(self, dbConnector, "helloworld")

    def getHelloWorldMessageByNum(self, num):
        cursor = self.getDBConnector().getCursor()
        cursor.callproc(self._daoConf["byNum"], [num])
        results = self._cursorResultsToJSon(next(cursor.stored_results()))
        if len(results) == 0:
                return ""
        return results[0]["message"]
