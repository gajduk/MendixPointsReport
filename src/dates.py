import datetime

date_formatt = "%Y-%m-%d"
datetime_formatt = "%Y-%m-%d %H:%M:%S"
begginingOfTime = datetime.datetime(1970,1,1)

class Dates(object):

	def getCurrentDay(self):
		return (datetime.datetime.utcnow() - begginingOfTime).days

	def getDayForDate(self,date):
		return (date - begginingOfTime).days

	def getDateForDay(self,day):
		return begginingOfTime+datetime.timedelta(days=day)

	def getDatestampForDate(self,date):
		return date.strftime(date_formatt)

	def getTimestampForDate(self,date):
		return date.strftime(datetime_formatt)

	def getTimestamp(self):
		return self.getTimestampForDate(datetime.datetime.utcnow())

class DatesWithOffset(Dates):

	def __init__(self,offset):
		self._offset = offset

	def getCurrentDay(self):
		return super(DatesWithOffset, self).getCurrentDay()+self._offset

	def getDayForDate(self,date):
		return super(DatesWithOffset, self).getDayForDate(date)+self._offset

	def getDateForDay(self,day):
		return super(DatesWithOffset, self).getDateForDay(day+self._offset)

	def getTimestampForDate(self,date):
		return super(DatesWithOffset, self).getTimestampForDate(date+datetime.timedelta(days=self._offset))

	def getDatestampForDate(self,date):
		return super(DatesWithOffset, self).getDatestampForDate(date+datetime.timedelta(days=self._offset))
