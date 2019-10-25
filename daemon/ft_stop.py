# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stop.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/25 17:34:18 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/25 17:55:35 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from app import ft_send
from app import App
import os,sys,signal,time,threading

def check_pid(pid):
	try:
		os.kill(pid, 0)
	except OSError:
		return False
	else:
		return True

def forcekill_timeout(app):
	sleeptime = 0.1
	i = 0
	while i < app.stoptime:
		if check_pid(app.pid) == False:
			break
		i += sleeptime
		time.sleep(sleeptime)
	if check_pid(app.pid):
		try:
			os.kill(app.pid, signal.SIGKILL)
		except OSError:
			pass
	app.status = "STOPED"
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
