import rethinkdb as r
import datetime
import dates

pointsTable = r.table("MendixPoints")

def savePoints(DisplayName,Points):
	currentDay = dates.getCurrentDay()
	previousPoints,deltaDays = _getPreviousPointsAndDeltaDays(currentDay,DisplayName)
	deltaPoints = {}
	if previousPoints:
		deltaPoints = {e:(Points[e]-previousPoints[e])*1.0/deltaDays for e in Points }

	pointsTable.insert([
		{
			"DisplayName": DisplayName,
			"TotalPoints": Points,
			"DeltaPoints": deltaPoints,
			"Day": currentDay
		}
	]).run()

def _getPreviousPointsAndDeltaDays(Day,DisplayName):
	try:
		previousPointsRecord = pointsTable.filter(r.row["Day"] < Day & r.row["DisplayName"] == DisplayName).limit(1)[0]
		return previousPointsRecord["TotalPoints"],Day-previousPointsRecord["Day"]
	except:
		pass

def queryPointsForUser(DisplayName,Date):
	queryDay = dates.getDayForDate(Date)
	return pointsTable.filter(r.row["Day"] == queryDay & r.row["DisplayName"] == DisplayName).limit(1)[0]