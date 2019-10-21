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
from daemon import handler
from daemon import daemon
from daemon import ft_builtins
from parse_cfgfile import validate

lst,socket_addr = validate()
handler.ft_handle_sigchild()
daemon.ft_daemon()
try :
	os.unlink("/tmp/socket")
except :
	pass
sock = init_socket.init_socket(socket_addr)

sock.listen(10)

def listener(conn):
	try :
		while True :
			data = conn.recv(2048)
			if data:
				array = pickle.loads(data)
				ft_builtins.ft_builtin(array, lst, conn)
			else:
				break
	finally:
		conn.close()

while 1:
	try:
		conn, addr = sock.accept()
		thr = threading.Thread(target=listener, args=(conn,))
		thr.start()
	except:
		pass
