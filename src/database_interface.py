import pymongo
from urllib import quote_plus
import database_credentials


class MongoDBInterface:
	#dates interfaces
	_dates = ''

	def __init__(self, dates):
		username = quote_plus(database_credentials.db_username)
		password = quote_plus(database_credentials.db_password)
		client = pymongo.MongoClient('mongodb://%s:%s@ds042417.mlab.com:42417/mendix-points-report' % (username, password))
		self._points_coll = client["mendix-points-report"]["MendixPointsMock"]
		self._dates = dates

	def savePoints(self,DisplayName,Points):
		currentDay = self._dates.getCurrentDay()
		previousPoints,deltaDays = self._getPreviousPointsAndDeltaDays(currentDay,DisplayName)
		deltaPoints = {}
		if previousPoints:
			deltaPoints = {e:(Points[e]-previousPoints[e])*1.0/deltaDays for e in Points }

		self._points_coll.find_one_and_update(
			{
				"DisplayName": DisplayName,
				"Day": currentDay
			},
			{
				"$set": {
							"TotalPoints": Points,
							"DeltaPoints": deltaPoints,
						}
			},
			upsert=True)

	def _getPreviousPointsAndDeltaDays(self,Day,DisplayName):
		try:
			previousPointsRecord = self._points_coll.find_one({
				"DisplayName" : DisplayName,
				"Day": {"$lt": Day }
			})
			return previousPointsRecord["TotalPoints"],Day-previousPointsRecord["Day"]
		except:
			return None,None

	def queryPointsForUser(self,DisplayName,Date):
		queryDay = self._dates.getDayForDate(Date)
		return points_coll.find_one({
				"DisplayName" : DisplayName,
				"Day": queryDay
			})
