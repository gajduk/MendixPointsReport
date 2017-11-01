from phantomjs.query_points_with_phantomjs import PhantomJSQuery
from database_interface import MongoDBInterface
from dates import Dates
from users_list import UsersList

class QueryPoints:
	#database interface
	_db = ''
	#query interface
	_query = ''
	_users_list = ''

	def __init__(self, db=MongoDBInterface(), query=PhantomJSQuery(), users_list=UsersList()):
		self._db = db
		self._query = query
		self._users_list = users_list

	def queryAndSavePointsForAllUsers(self):
		users = self._users_list.getUsers()
		for user in users:
			points = self._query.getCurrentPointsForUser(user)
			self._db.savePoints(user,points)

def main():
	QueryPoints().queryAndSavePointsForAllUsers()

if __name__ == "__main__":
	main()
