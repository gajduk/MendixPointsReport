import pymongo
from urllib import quote_plus
import database_credentials
from dates import Dates

class MongoDBInterface:
	#dates interfaces
	_dates = ''
	#database connector
	_db = ''

	def __init__(self, dates=Dates(), useTestColl=True):
		username = quote_plus(database_credentials.db_username)
		password = quote_plus(database_credentials.db_password)
		client = pymongo.MongoClient('mongodb://%s:%s@ds042417.mlab.com:42417/mendix-points-report' % (username, password))
		self._db = client["mendix-points-report"]
		if useTestColl:
			self._points_coll = self._db["MendixPointsMock"]
		else:
			self._points_coll = self._db["MendixPoints"]
		self._dates = dates

	def getDB(self):
		return self._db

	def savePoints(self,DisplayName,Points):
		currentDay = self._dates.getCurrentDay()
		previousPoints,deltaDays = self._getPreviousPointsAndDeltaDays(currentDay,DisplayName)
		deltaPoints = {}
		if previousPoints:
			deltaPoints = {e:(Points[e]-previousPoints[e])*1.0/deltaDays for e in Points }
			for day in range(1,deltaDays):
				self._points_coll.find_one_and_update(
					{
						"Name": DisplayName,
						"Day": currentDay-day
					},
					{
						"$set": {
									"DeltaPoints": deltaPoints,
									"Inferred": True,
									"Timestamp": self._dates.getTimestampForDate(self._dates.getDateForDay(currentDay-day))
								}
					},
					upsert=True)
		self._points_coll.find_one_and_update(
			{
				"Name": DisplayName,
				"Day": currentDay
			},
			{
				"$set": {
							"TotalPoints": Points,
							"DeltaPoints": deltaPoints,
							"Inferred": deltaDays>1,
							"Timestamp": self._dates.getTimestamp()
						}
			},
			upsert=True)

	def _getPreviousPointsAndDeltaDays(self,Day,DisplayName):
		try:
			previousPointsRecord = self._points_coll.find({
				"Name" : DisplayName,
				"Day": {"$lt": Day }
			}).sort([("Day",-1)]).limit(1).next()
			return previousPointsRecord["TotalPoints"],Day-previousPointsRecord["Day"]
		except:
			return None,None

	def queryPointsForUserForSingleDate(self,DisplayName,Date):
		queryDay = self._dates.getDayForDate(Date)
		res = self._points_coll.find_one({
				"Name" : DisplayName,
				"Day": queryDay
			})
		if res:
			return {"DeltaPoints":res["DeltaPoints"],
					"Inferred":res["Inferred"],
					"Date":self._dates.getDateForDay(res["Day"])}
		else:
			return None

	def queryPointsForUserForAPeriod(self,DisplayName,PeriodStart,PeriodEnd):
		startDay = self._dates.getDayForDate(PeriodStart)
		endDay = self._dates.getDayForDate(PeriodEnd)
		print startDay,endDay
		res = self._points_coll.find({
				"Name" : DisplayName,
				"Day": { "$gte" : startDay, "$lt" : endDay }
			})
		if res:
			return [{"DeltaPoints":e["DeltaPoints"],
					"Inferred":e["Inferred"],
					"Date":self._dates.getDateForDay(e["Day"])} for e in res]
		else:
			return []
