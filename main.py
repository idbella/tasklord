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
from daemon import handler
from app import App

logger.init_logger()
lst,socket_addr = validate(True)
sock = init_socket.init_socket(socket_addr)
daemon.ft_daemon()
logger.log("daemon started\n")
App.lst = lst
App.socket = sock
signal.signal(signal.SIGCHLD, handler.handler)
sock.listen(10)
builtins.ft_startup()

while 1:
	conn = None
	if App.shutdown:
		break
	try:
		conn, addr = App.socket.accept()
	except:
		pass
	if conn:
		logger.log("new Connection\n")
		thr = threading.Thread(target=listener.listen, args=(conn,))
		thr.start()
