import json
import sys
import os

def loadjson():
	argc = len(sys.argv)
	if argc < 2 :
		print("not config file is provided")
		exit(1)
	configfile = sys.argv[1]
	if os.path.exists(configfile) == False :
		print(configfile + " no such file or directory")
		exit(1)
	if os.path.isfile(configfile) == False :
		print(configfile + " is a directory")
		exit(1)
	with open(configfile) as file:
		try :
			lst = json.load(file)
			socket = lst['socket']
		except :
			print(configfile + " not a valid json file")
			exit(1)
	return lst
