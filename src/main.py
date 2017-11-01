from logger import log
import traceback
from database_interface import MongoDBInterface
from dates import Dates
from users_list import UsersList
from query_points import QueryPoints
from phantomjs.query_points_with_phantomjs import PhantomJSQuery

def queryPointsAndSave(db,users_list):
    query_backend = PhantomJSQuery()
    query_executor = QueryPoints(db=db,query=query_backend,users_list=users_list)
    log("Started querying")
    query_res = query_executor.queryAndSavePointsForAllUsers()
    log("Querying finished:"+str(query_res))

def main():
    try:
        log("Started main")
        db = MongoDBInterface(dates=Dates(), useTestColl=False)
        users_list = UsersList()
        queryPointsAndSave(db,users_list)
    except Exception as e:
        log(traceback.format_exc(),error=True)

if __name__ == "__main__":
    main()
