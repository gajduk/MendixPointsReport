
class UsersList:

    def __init__(self,users_file="users.txt"):
        self._users_file = users_file

    def getUsers(self):
        res = []
    	with open(self._users_file,"r") as pin:
    		res = [line for line in pin]
    	return res


class AndrejGajdukUsersList:

    def getUsers(self):
        return ["Andrej Gajduk"]
