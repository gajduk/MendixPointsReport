import time
from subprocess import check_output
from os import listdir
from os.path import isfile, join
import json

phantom_js = "phantom_getuserstats.js"

def getCurrentPointsForUser(DisplayName):
	res = check_output(["phantomjs", phantom_js, DisplayName])
	return res

def main():
	print getCurrentPointsForUser("Andrej Gajduk")

if __name__ == "__main__":
	main()