#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yoyassin <yoyassin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 15:27:18 by yoyassin          #+#    #+#              #
#    Updated: 2019/10/12 15:27:35 by yoyassin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys, time, signal, pickle
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
			data = bytes(conn.recv(96))
			if data:
				array = pickle.loads(data)
				print("data : {}" .format(array))
				ft_builtins.ft_builtin(array, l['apps'], conn)
			else:
				print("not receiving anything.")
				break
	finally:
		conn.close()

while 1:
	conn, addr = sock.accept()
	thr = threading.Thread(target=listener, args=(conn,))
	thr.start()
