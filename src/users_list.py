import json
from database_interface import MongoDBInterface

class UsersListJsonFile:

    def __init__(self,users_file="users.json"):
        self._users_file = users_file

    def getUsers(self):
        return json.load(open(self._users_file,"r"))

class UsersListDB:

    _db = ''

    def __init__(self,db=MongoDBInterface(),users_coll="Users"):
        self._db = db
        self._users_coll = users_coll

    def getUsers(self):
        return [e for e in self._db.getDB()[self._users_coll].find()]


class AndrejGajdukUsersList:

    def getUsers(self):
        return [{"RealName":"Andrej Gajduk", "DisplayName":"Andrej Gajduk"}]

def main():
    print UsersListJsonFile().getUsers()
    print UsersListDB().getUsers()
    print AndrejGajdukUsersList().getUsers()

if __name__ == "__main__":
    main()
