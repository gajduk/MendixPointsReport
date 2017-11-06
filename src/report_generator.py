from database_interface import MongoDBInterface
from users_list import UsersListDB
from datetime import datetime,timedelta
date_formatt_weekly_report = "%a %d.%m"
class ReportGenerator:

    def __init__(self,db,users_list):
        self._db = db
        self._users_list = users_list

    def getLastWeekReport(self):
        last_weekpoints = self._getLastWeekPoints()
        return self._formatLastWeekPointsAaHTMLTable(last_weekpoints)

    def _formatLastWeekPointsAaHTMLTable(self,points):
        header = "<th>Category\Day</th>"
        header += "".join(["<th>"+e.strftime(date_formatt_weekly_report)+"</th>" for e in points["Dates"]])
        header = "<tr>"+header+"</tr>"
        rows = {c:"".join(['<td align="right">'+str(round(val, 1))+"</td>" for val in points["Points"][c]]) for c in points["Points"]}
        body = "".join(["<tr><td>"+c+"</td>"+rows[c]+"</tr>" for c in rows])
        return '<table border="1" cellspacing="0">'+header+body+"</table>"

    def _getLastWeekPoints(self):
        start_date,end_date = DatesHelper().getLastWeekPeriod()
        lastWeekPoints = self._db.queryPointsForUserForAPeriod("Andrej Gajduk",start_date,end_date)
        categories = sorted([c for c in lastWeekPoints[0]["DeltaPoints"]])
        dates = sorted([points["Date"] for points in lastWeekPoints])
        res = {"Dates":dates,"Points":{}}
        for c in categories:
            res["Points"][c] = [points["DeltaPoints"][c] for points in lastWeekPoints]
        return res


class DatesHelper:

    def getLastWeekPeriod(self):
        now = datetime.utcnow()
        return now-timedelta(days=7),now

def main():
    db = MongoDBInterface()
    users_list = UsersListDB()
    print ReportGenerator(db,users_list).getLastWeekReport()

if __name__ == "__main__":
    main()
