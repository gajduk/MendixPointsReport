import time
from subprocess import check_output
from os import listdir
from os.path import isfile, join
import json
import datetime

date_formatt = "%m_%d_%y"
data_folder = "data"
js_to_inject  "js_mxgetmyuser.js"
phantom_js = "phantom_getuserstats.js"
json_prefix = "userstats"
historic_data = "HistoryUserStat.json"

def runScriptAndWriteResult():
	timestamp =  datetime.datetime.today().strftime(date_formatt)
	res = check_output(["phantomjs", phantom_js])
	with open(json_prefix+timestamp+".json","w") as pout:
		pout.write(res)

def generateHistory():
	history = {}
	history_output = {}
	keys = ["TotalCommunityPoints","TotalForumPoints"
		,"TotalAppstorePoints","TotalPlatformPoints","TotalLearningPoints"]
	onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
	for file in onlyfiles:
		if file.startswith(json_prefix):
			date = datetime.datetime.strptime(file[9:17],date_formatt)
			try:
				with open(file,"r") as pin:
					temp = json.load(pin)[0]["jsonData"]["attributes"]
					to_add = {}
					for key in keys:
						if key in temp:
							to_add[key] = temp[key]["value"]
					history[date] = to_add
					history_output[file[9:17]] = to_add
			except:
				print "Could not parse file "+file
	with open(historic_data,"w") as pout:
		pout.write(json.dumps(history_output))
	return history

def loadHistory():
	with open(historic_data,"r") as pin:
		return json.load(pin)

def main():
	print loadHistory()

if __name__ == "__main__":
	main()