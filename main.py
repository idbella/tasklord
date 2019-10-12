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
import threading

from daemon import loader
from daemon import init_socket
from daemon import validate
from daemon import handler
from daemon import daemon
from daemon import ft_builtins

l = loader.loadjson()
validate.validate(l)
handler.ft_handle_sigchild()
daemon.ft_daemon()
sock = init_socket.init_socket(l['socket'])

sock.listen(10)

def listener(conn):
	try :
		while True :
			data = conn.recv(16)
			if data:
				data = str(data, 'UTF-8').lower()
				print("\n" + data)
				ft_builtins.ft_builtin(data, l['apps'], conn)
			else:
				print("not receiving anything from {}".format(client_addr))
				break
	finally:
		conn.close()

while 1:
	conn, addr = sock.accept()
	thr = threading.Thread(target=listener, args=(conn,))
	thr.start()
