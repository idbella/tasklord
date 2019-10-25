# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    runner.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 16:39:58 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/24 23:59:10 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, time, logger
from app import ft_send
from app import App

def run(app):
	if os.path.exists(app.argv[0]) == False :
		app.status = "FAILED";
	else:
		pid = os.fork()
		if pid == 0:
			os.chdir(app.workingdir)
			if app.stdout:
				fd = os.open(app.stdout, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
				os.dup2(fd, 1)
			if app.stderr:
				fd = os.open(app.stderr, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
				os.dup2(fd, 2)	
			os.umask(app.umask)
			os.execve(app.argv[0], app.argv, app.env)
			logger.log("error\n")
			exit(1)
		elif pid > 0:
			app.pid = pid
			app.started_at = int(time.time())
			app.status = "RUNNING"
			app.state = App.RUNNING
		else:
			app.status = "FORK FAILED"
	return app.status