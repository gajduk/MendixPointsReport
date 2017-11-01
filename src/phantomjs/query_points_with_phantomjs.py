import time
from subprocess import check_output
from os import listdir
from os.path import isfile, join
import json

class PhantomJSQuery:
	_phantom_js = join("phantomjs","phantom_getuserstats.js")

	def getCurrentPointsForUser(self,DisplayName):
		res = check_output(["phantomjs", self._phantom_js, DisplayName])
		return json.loads(res)

class MockQuery:

	def __init__(self,points):
		self._points = points

	def getCurrentPointsForUser(self,DisplayName):
		return self._points

def main():
	print PhatnomJSQuery().getCurrentPointsForUser("Andrej Gajduk")

if __name__ == "__main__":
	main()
