from phantomjs.query_points_with_phantomjs import PhantomJSQuery
from database_interface import MongoDBInterface
from dates import Dates

class QueryPoints:
	#database interface
	_db = ''
	#query interface
	_query = ''
	_users_file = ''

	def __init__(self, db, query, users_file="users.txt"):
		self._db = db
		self._query = query
		self._users_file = users_file

	def getQueriedUsers(self):
		res = []
		with open(self._users_file,"r") as pin:
			res = [line for line in pin]
		return res

	def queryAndSavePointsForAllUsers(self):
		users = self.getQueriedUsers()
		for user in users:
			points = self._query.getCurrentPointsForUser(user)
			self._db.savePoints(user,points)

def main():
	QueryPoints(MongoDBInterface(Dates()),PhantomJSQuery()).queryAndSavePointsForAllUsers()

if __name__ == "__main__":
	main()
