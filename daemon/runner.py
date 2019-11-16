# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    runner.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yoyassin <yoyassin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 16:39:58 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/16 14:19:00 by yoyassin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, time, logger, signal
from app import ft_send
from app import App

def run(app):
	if os.path.exists(app.argv[0]) == False :
		logger.log("{} command not found\n".format(app.argv[0]))
		app.status = "FAILED"
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
			logger.log("umask : {}\n".format(app.umask))
			try:
				os.execve(app.argv[0], app.argv, app.env)
			except:
				logger.log("Error launching program.\n")
			os.kill(os.getpid(), signal.SIGKILL)
		elif pid > 0:
			app.pid = pid
			app.started_at = int(time.time())
			app.status = "RUNNING"
			app.state = App.RUNNING
		else:
			app.status = "FAILED"
	return app.status