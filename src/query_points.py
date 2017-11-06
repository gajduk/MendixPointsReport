from phantomjs.query_points_with_phantomjs import PhantomJSQuery
from database_interface import MongoDBInterface
from dates import Dates
from users_list import UsersListDB

class QueryPoints:
	#database interface
	_db = ''
	#query interface
	_query = ''
	_users_list = ''

	def __init__(self, db=MongoDBInterface(), query=PhantomJSQuery(), users_list=UsersListDB()):
		self._db = db
		self._query = query
		self._users_list = users_list

	def queryAndSavePointsForAllUsers(self):
		users = self._users_list.getUsers()
		res = []
		for user in users:
			points = self._query.getCurrentPointsForUser(user["DisplayName"])
			self._db.savePoints(user["RealName"],points)
			res.append({"user":user,"points":points})
		return res

def main():
	QueryPoints().queryAndSavePointsForAllUsers()

if __name__ == "__main__":
	main()
