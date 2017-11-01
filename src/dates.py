import datetime

date_formatt = "%d_%m_%y"

begginingOfTime = datetime.datetime(1970,1,1)

def getCurrentDay():
	return getDayForDate(datetime.datetime.utcnow())

def getDayForDate(date):
	return (date - begginingOfTime).days

def getDateForDay(day):
	return begginingOfTime+timedelta(days=day) 

def getTimestampForDate(date):
	return date.strftime(date_formatt)