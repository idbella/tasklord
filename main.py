#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 15:27:18 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/12 15:27:35 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, time, signal
import threading, pickle

from daemon import loader
from daemon import init_socket
from daemon import validate
from daemon import daemon
from daemon import listener
from parse_cfgfile import validate
from daemon import builtins
import logger
from app import App

logger.init_logger()
lst,socket_addr = validate()
sock = init_socket.init_socket(socket_addr)
daemon.ft_daemon()
logger.log("daemon started\n")

def handler(sig, fr):
	while True:
		pid, status = os.waitpid(-1, os.WNOHANG)
		exitstatus = os.WEXITSTATUS(status)
		if pid <= 0:
			break
		for app in lst:
			if app.pid == pid:
				logger.log("app " + app.name + " exited with status " + str(exitstatus) + "\n")
				app.status = "DONE"
				if app.state != app.DONE and exitstatus not in app.exitcodes:
					logger.log("unexpected\n")
					app.state = App.STOPED
					if app.autorestart == "unexpected" or app.autorestart == "always":
						app.failtimes += 1
						builtins.ft_start(lst, sock, [app.name], False)

signal.signal(signal.SIGCHLD, handler)
sock.listen(10)
builtins.ft_startup(lst, sock)
while 1:
	try:
		conn, addr = sock.accept()
		thr = threading.Thread(target=listener.listen, args=(conn,lst))
		thr.start()
	except:
		pass
