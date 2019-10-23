# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    builtins.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 19:23:05 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/23 19:07:32 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, time, signal, threading, copy
from daemon import runner
from app import ft_send
from app import App
import logger, datetime

def forcekill_timeout(app):
	sleeptime = 0.2
	i = 0
	while i < app.stoptime:
		if app.status != "RUNNING":
			break
		i += sleeptime
		time.sleep(sleeptime)
	if app.status == "RUNNING":
		try:
			os.kill(app.pid, signal.SIGKILL)
		finally:
			app.status = "STOPED"

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

def ft_stop(sock, args, wait):
	all = "all" in args
	for app in App.lst:
		if (all or app.name in args) and app.status == "RUNNING":
			ft_send("stopping " + app.name + "...\n", sock)
			os.kill(app.pid, app.stopsignal)
			app.state = App.DONE
			if wait:
				forcekill_timeout(app)
			else:
				thr = threading.Thread(target=forcekill_timeout, args=(app,))
				thr.start()

def ft_start(sock, args, log):
	all = "all" in args
	for app in App.lst:
		if (all or app.name in args) and app.status != "RUNNING":
			if log:
				ft_send("running " + app.name + "\n", sock)
			logger.log("running {}\n".format(app.name))
			runner.run(app)

def ft_restart(sock, args):
	ft_stop(sock, args, True)
	ft_start(sock, args, True)

def ft_builtin(data, sock):
	cmd = data[0]
	del data[0]
	if cmd == "status":
		ft_status(sock, data)
	elif cmd == "start":
		ft_start(sock, data, True)
	elif cmd == "stop":
		ft_stop(sock, data, False)
	elif cmd == "restart":
		ft_restart(sock, data)

def ft_startup():
	for app in App.lst:
		if app.autostart:
			ft_start(None, [app.name], False)
