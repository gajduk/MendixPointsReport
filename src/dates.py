import datetime

date_formatt = "%d_%m_%y"
begginingOfTime = datetime.datetime(1970,1,1)

class Dates:

	def getCurrentDay(self):
		return self.getDayForDate(datetime.datetime.utcnow())

	def getDayForDate(self,date):
		return (date - begginingOfTime).days

	def getDateForDay(self,day):
		return begginingOfTime+timedelta(days=day)

	def getTimestampForDate(self,date):
		return date.strftime(date_formatt)

class DatesWithOffset(Dates):

	def __init__(self,offset):
		self._offset = offset

	def getCurrentDay(self):
		return super(DatesWithOffset, self).getCurrentDay()+self._offset

	def getDayForDate(self,date):
		return super(DatesWithOffset, self).getDayForDate(date)+self._offset

	def getDateForDay(self,day):
		return super(DatesWithOffset, self).getDateForDay(day+self._offset)
