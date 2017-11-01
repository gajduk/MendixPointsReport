from database_interface import MongoDBInterface
from users_list import UsersList
from datetime import datetime

def main():
    db = MongoDBInterface()
    print db.queryPointsForUser("Andrej Gajduk",datetime(2017,10,25))

if __name__ == "__main__":
    main()
