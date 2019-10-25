# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    builtins.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 19:23:05 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/25 18:16:48 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, time, signal, threading, copy
from daemon import runner
from app import ft_send
from app import App
import logger, datetime
from daemon import reload
from daemon import ft_stop

def ft_status(sock, args):
	all = "all" in args or len(args) == 0
	ft_send('\n+{}+\n| {:20}| {:8}| {:16}| {:9}|\n+{}+\n'.format('-'*60, "NAME", "PID", "STATUS", "DURATION",'-'*60), sock)
	for app in App.lst:
		if all or app.name in args:
			pid = app.pid
			if app.status == "RUNNING":
				uptime = int(time.time() - app.started_at)
			else:
				uptime = 0
				pid = "-----"
			uptime = datetime.timedelta(seconds=uptime)
			ft_send("| {:20}| {:8}| {:16}| {:9}|\n".format(app.name, str(pid), app.status, str(uptime)), sock)
	ft_send('+{}+\n\n'.format('-'*60), sock)

def ft_start(sock, args, log):
	all = "all" in args
	for app in App.lst:
		if (all or app.name in args) and app.status != "RUNNING":
			if log:
				ft_send("running " + app.name + "\n", sock)
			logger.log("running {}\n".format(app.name))
			runner.run(app)

def ft_restart(sock, args):
	ft_stop.ft_stop(sock, args, True)
	ft_start(sock, args, True)

def ft_builtin(data, sock):
	cmd = data[0]
	del data[0]
	if cmd == "status":
		ft_status(sock, data)
	elif cmd == "start":
		ft_start(sock, data, True)
	elif cmd == "stop":
		ft_stop.ft_stop(sock, data, False)
	elif cmd == "restart":
		ft_restart(sock, data)
	elif cmd == "reload":
		restart_list = reload.reload(sock)
		if restart_list != None:
			ft_restart(sock, restart_list)
			ft_startup()

def ft_startup():
	for app in App.lst:
		if app.autostart:
			ft_start(None, [app.name], False)
