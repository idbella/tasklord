# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stop.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/25 17:34:18 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/15 22:42:10 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from app import ft_send
from app import App
import os,sys,signal,time,threading
from logger import log

def check_pid(pid):
	try:
		os.kill(pid, 0)
	except OSError:
		return False
	return True

def forcekill_timeout(app):
	sleeptime = 0.1
	i = 0
	while i < app.stoptime:
		if check_pid(app.pid) == False:
			return
		i += sleeptime
		time.sleep(sleeptime)
	if check_pid(app.pid):
		try:
			os.kill(app.pid, signal.SIGKILL)
		except OSError:
			pass
	app.status = "STOPED"

def ft_stop(sock, args, wait, shutdown):
	all = "all" in args
	for app in App.lst:
		if (all or app.name in args) and app.status == "RUNNING":
			ft_send("stopping " + app.name + "...\n", sock)
			app.state = App.DONE
			try:
				if shutdown:
					os.kill(app.pid, signal.SIGTERM)
				else:
					os.kill(app.pid, app.stopsignal)
			except OSError:
				pass
			if wait:
				forcekill_timeout(app)
			else:
				thr = threading.Thread(target=forcekill_timeout, args=(app,))
				thr.start()
