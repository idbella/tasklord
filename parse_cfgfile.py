# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse_cfgfile.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 16:15:41 by yoyassin          #+#    #+#              #
#    Updated: 2019/10/21 14:25:54 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import loader as l
import app as proc
import sys, os, copy

def validate():
    cfg_file = l.loadjson()
    keys = cfg_file.keys()
    if len(keys) > 2 :
        print("Extra field.")
        sys.exit(1)
    elif 'socket' not in keys or 'apps' not in keys:
        print("Missing field or wrong field.")
        sys.exit(1)
    app = cfg_file['apps']
    procs_list = []
    for i in range(len(app)):
        process = proc.App()
        try :
            process.name = app[i]['name']
            process.cmd = app[i]['cmd']
        except:
            print("Invalid json file.", file=sys.stderr)
            sys.exit(1)
        process.numprocs = app[i].get('numprocs', 1)
        process.umask = app[i].get('umask', 644)
        process.workingdir = app[i].get('workingdir', '/tmp')
        process.autostart = app[i].get('autostart')
        process.autorestart = app[i].get('autorestart', 'unexpected')
        process.exitcodes = app[i].get('exitcodes', [0])
        process.startretries = app[i].get('startretries', 1)
        process.starttime = app[i].get('starttime', 0)
        process.stopsignal = app[i].get('stopsignal', 15)
        process.stoptime = app[i].get('stoptime', 10)
        process.stdout = app[i].get('stdout')
        process.env = app[i].get('env', [])
        for id in range(process.numprocs):
            name = process.name;
            if process.numprocs > 1:
                name = process.name + ":" + process.name + str(id);
            new = copy.copy(process)
            new.name = name;
            procs_list.append(new)
    return procs_list, cfg_file['socket']
