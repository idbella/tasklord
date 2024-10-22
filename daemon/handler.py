# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    handler.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:17:37 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/15 22:25:31 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal, os, sys, time
from app import App
import logger
from daemon import builtins

def handler(sig, frame):
	lst = App.lst
	while True:
		try:
			pid, status = os.waitpid(-1, os.WNOHANG)
		except:
			break
		if pid <= 0:
			break
		exitcode = os.WEXITSTATUS(status)
		for app in lst:
			if app.pid == pid:
				if os.WIFEXITED(status):
					logger.log("app " + app.name + " exited with status " + str(exitcode) + "\n")
				else:
					logger.log("app {} recieved signal {}\n".format(app.name, os.WTERMSIG(status)))
				app.status = "STOPED"
				if app.state != app.DONE:
					app.status = "DONE"
					uptime = time.time() - app.started_at
					if uptime < app.starttime:
						if app.failtimes < app.startretries:
							app.failtimes += 1
							logger.log("failed to run {} for {} seconds Retry {}\n".format(app.name, str(app.starttime), app.failtimes))
							logger.log("retry {} \n".format(app.name))
							builtins.ft_start(None, [app.name], False)
							break
						else:
							logger.log("failed to run {} {} times for {} seconds\n".format(app.name, str(app.startretries), app.starttime))
							logger.log("abort {} \n".format(app.name))
							app.status = "ABORTED"
							app.state = App.DONE
					elif (app.autorestart == "unexpected" and (exitcode not in app.exitcodes or os.WIFSIGNALED(status))) or app.autorestart == "always":
						if not os.WIFSIGNALED(status) and exitcode not in app.exitcodes:
							logger.log("app {} exited with unexpected exit code [{}]\n".format(app.name, exitcode))
						app.state = App.STOPED
						if app.autorestart == "unexpected" or app.autorestart == "always":
							logger.log("auto restart {}\n".format(app.name))
							builtins.ft_start(None, [app.name], False)
					app.failtimes = 0
				else:
					app.state = App.STOPED
				break
