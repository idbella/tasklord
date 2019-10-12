import loader as l
import app as proc
import sys

def validate():
    cfg_file = l.loadjson()
    keys = cfg_file.keys()
    if len(keys) > 2 :
        print("Extra field.")
        sys.exit(1)
    elif 'socket' not in keys or 'apps' not in keys:
        print("Missing fields or wrong field.")
        sys.exit(1)
    app = cfg_file['apps']
    procs_list = []
    for i in range(len(app)):
        process = proc.App()
        process.name = app[i]['name']
        process.numprocs = app[i]['numprocs']
        process.umask = app[i]['umask']
        process.workingdir = app[i]['workingdir']
        process.autostart = app[i]['autostart']
        process.autorestart = app[i]['autorestart']
        process.exitcodes = app[i]['exitcodes']
        process.startretries = app[i]['startretries']
        process.starttime = app[i]['starttime']
        process.stopsignal = app[i]['stopsignal']
        process.stoptime = app[i]['stoptime']
        process.stdout = app[i]['stdout']
        process.env = app[i]['env']
        procs_list.append(process)
    print(vars(procs_list[1]))
    return procs_list
validate()