# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    handler.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:17:37 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/23 19:23:18 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal, os, sys, time
from app import App
import logger
from daemon import builtins

def handler(sig, unknown):
	lst = App.lst
	while True:
		pid, status = os.waitpid(-1, os.WNOHANG)
		exitcode = os.WEXITSTATUS(status)
		if pid <= 0:
			break
		for app in lst:
			if app.pid == pid:
				logger.log("app " + app.name + " exited with status " + str(exitcode) + "\n")
				app.status = "DONE"
				if app.state != app.DONE:
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
					elif exitcode not in app.exitcodes:
						logger.log("app {} exited with unexpected exit code [{}]\n".format(app.name, exitcode))
						app.state = App.STOPED
						if app.autorestart == "unexpected" or app.autorestart == "always":
							logger.log("auto restart {}\n".format(app.name))
							builtins.ft_start(None, [app.name], False)
					app.failtimes = 0
				else:
					app.state = App.STOPED
				break
