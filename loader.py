import json
import sys
import os

def loadjson(exit_on_error):
    error = False
    argc = len(sys.argv)
    if argc < 2 :
        error = "No config file is provided."
    if error == False:
        configfile = sys.argv[1]
        if os.path.exists(configfile) == False:
            error = configfile + " no such file or directory"
        if error == False and os.path.isfile(configfile) == False :
            error = configfile + " is a directory"
        if error == False:
            with open(configfile) as file:
                try :
                    lst = json.load(file)
                    socket = lst['socket']
                except :
                    error = configfile + " not a valid json file"
    if error == False:
        return True, lst
    if exit_on_error:
        print(error)
        exit(1)
    return False, error
