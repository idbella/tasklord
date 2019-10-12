class App:
    pid = 0
    name = None
    numprocs = 1
    umask = 644
    workingdir = "/tmp"
    autostart = False
    autorestart = "unexpected"
    exitcodes = [0]
    startretries = 1
    starttime = 0
    stopsignal = 15
    stoptime = 10
    stdout = None
    env = []