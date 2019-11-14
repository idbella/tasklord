# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reload.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/23 19:29:21 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/14 15:29:19 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from parse_cfgfile import validate
from app import ft_send
from app import App
import logger
from daemon import ft_stop

def reload(socket):
    lst,socket_addr = validate(False)
    if lst == False:
        ft_send(socket_addr + "\n", socket)
        return None, None
    if (socket_addr == False):
        ft_send(lst, socket)
        return None, None
    restart_list = [];
    for app1 in App.lst:
        found = False
        for app2 in lst:
            if app1.original_name == app2.original_name:
                found = True
                restart = False
                if app1.cmd != app2.cmd:
                    restart = True
                if app1.workingdir != app2.workingdir:
                    restart = True
                if app1.stdout != app2.stdout:
                    restart = True
                if app1.stderr != app2.stderr:
                    restart = True
                if app1.numprocs != app2.numprocs:
                    restart = True
                if app1.umask != app2.umask:
                    restart = True
                if restart == True and app1.status == "RUNNING":
                    restart_list.append(app1.name)
                if app1.name == app2.name:
                    app2.status = app1.status
                    app2.state = app1.state
                    app2.pid = app1.pid
                    app2.started_at = app1.started_at
        if found == False:
            ft_stop.ft_stop(socket, [app1.name], False)
    App.lst = lst
    return restart_list
