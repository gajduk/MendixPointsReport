from phantomjs.query_points_with_phantomjs import getCurrentPointsForUser
import database_interfaces as db

def getQueriedUsers():
	res = []
	with open("users.txt","r") as pin:
		res = [line for line in pin]
	return res

def queryAndSavePointsForAllUsers():
	users = getQueriedUsers()
	for user in users:
		points = getCurrentPointsForUser(user)
		db.savePoints(user,points)

