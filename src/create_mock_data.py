from query_points import QueryPoints
from phantomjs.query_points_with_phantomjs import MockQuery
from database_interface import MongoDBInterface
from dates import DatesWithOffset

def addRecord(Points,DayOffset):
    db = MongoDBInterface(DatesWithOffset(DayOffset))
    query = MockQuery(Points)
    QueryPoints(db,query).queryAndSavePointsForAllUsers()

def main():
    addRecord({
        "Platform": 22,
        "Appstore": 13,
        "Forum": 10,
        "Community": 0,
        "Learning": 0
    },-300)
    addRecord({
        "Platform": 2022,
        "Appstore": 213,
        "Forum": 2010,
        "Community": 0,
        "Learning": 374
    },-30)
    addRecord({
        "Platform": 2122,
        "Appstore": 313,
        "Forum": 2110,
        "Community": 0,
        "Learning": 374
    },-10)
    addRecord({
        "Platform": 2522,
        "Appstore": 313,
        "Forum": 2210,
        "Community": 0,
        "Learning": 374
    },-7)
    addRecord({
        "Platform": 2522,
        "Appstore": 313,
        "Forum": 2230,
        "Community": 0,
        "Learning": 374
    },-5)
    addRecord({
        "Platform": 2528,
        "Appstore": 318,
        "Forum": 2232,
        "Community": 0,
        "Learning": 374
    },-4)
    addRecord({
        "Platform": 2530,
        "Appstore": 320,
        "Forum": 2232,
        "Community": 0,
        "Learning": 375
    },-3)
    addRecord({
        "Platform": 2540,
        "Appstore": 322,
        "Forum": 2272,
        "Community": 0,
        "Learning": 375
    },-1)
    addRecord({
        "Platform": 2542,
        "Appstore": 325,
        "Forum": 2276,
        "Community": 2,
        "Learning": 376
    },0)

if __name__ == "__main__":
    main()
