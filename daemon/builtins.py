# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    builtins.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 19:23:05 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/23 00:24:20 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, time, signal, threading
from daemon import runner
from app import ft_send
from app import App
import logger, datetime

def forcekill_timeout(app):
	time.sleep(app.stoptime)
	if app.status == "RUNNING":
		try:
			os.kill(app.pid, signal.SIGKILL)
		finally:
			app.status = "STOPED"

def ft_status(lst, sock, args):
	del args[0]
	all = "all" in args or len(args) == 0
	ft_send('\n+{}+\n| {:20}| {:8}| {:16}| {:9}|\n+{}+\n'.format('-'*60, "NAME", "PID", "STATUS", "DURATION",'-'*60), sock)
	for app in lst:
		if all or app.name in args:
			pid = app.pid
			if app.status == "RUNNING":
				uptime = int(time.time() - app.started_at)
				pid = "-----"
			else:
				uptime = 0
			uptime = datetime.timedelta(seconds=uptime)
			ft_send("| {:20}| {:8}| {:16}| {:9}|\n".format(app.name, str(pid), app.status, str(uptime)), sock)
	ft_send('+{}+\n\n'.format('-'*60), sock)

def ft_stop(lst, sock, args):
	del args[0]
	all = "all" in args or len(args) == 0
	for app in lst:
		if (all or app.name in args) and app.status == "RUNNING":
			ft_send("stopping " + app.name + "...\n", sock)
			os.kill(app.pid, app.stopsignal)
			app.state = App.DONE
			thr = threading.Thread(target=forcekill_timeout, args=(app,))
			thr.start()

def ft_start(lst, sock, args, log):
	del args[0]
	all = "all" in args or len(args) == 0
	for app in lst:
		if (all or app.name in args) and app.status != "RUNNING":
			if log:
				ft_send("running " + app.name + "\n", sock)
			runner.run(app, sock)
		else:
			logger.log("no\n")

def ft_builtin(data, lst, sock):
	if data[0] == "status":
		ft_status(lst, sock, data)
	elif data[0] == "start":
		ft_start(lst, sock, data, True)
	elif data[0] == "stop":
		ft_stop(lst, sock, data)

def ft_startup(lst, sock):
	for app in lst:
		if app.autostart:
			runner.run(app, sock)