# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    runner.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 16:39:58 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/13 16:58:00 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def run(app, sock):
	if os.path.exists(app.cmd) == False :
		ft_send("file " + app.cmd + " not found", sock)
	else:
		pid = os.fork()
		if pid == 0:
			print(app.env)
			if app.stdout:
				fd = os.open(app.stdout, os.O_WRONLY | os.O_CREAT)
				os.dup2(fd, 1)
			if app.stderr:
				fd = os.open(app.stderr, os.O_WRONLY | os.O_CREAT)
				os.dup2(fd, 2)
			os.chdir(app.workingdir)
			os.umask(app.umask)
			os.execve(app.cmd, ["df"], app.env)
			exit(1)
