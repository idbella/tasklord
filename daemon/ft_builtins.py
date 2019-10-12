# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_builtins.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 19:23:05 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/12 19:54:45 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys

def run(app, sock):
		ft_send("running " + app['name'], sock)
		if os.path.exists(app['cmd']) == False :
			ft_send("file " + app['cmd'] + " not found", sock)
		else:
			pid = os.fork()
			if pid == 0:
				os.execv(app['cmd'], ["df"])

def ft_send(msg, sock):
	msgutf8 = bytes(msg, 'UTF-8')
	sock.sendall(msgutf8)

def ft_status(lst, sock, args):
	for app in lst:
		ft_send("status of " + app['name'], sock)

def ft_stop(lst, sock, args):
	for app in lst:
		ft_send("stopping " + app['name'], sock)

def ft_start(lst, sock, args):
	for app in lst:
		run(app, sock)

def ft_builtin(data, lst, sock):
	if data == "status":
		ft_status(lst, sock, "")
	elif data == "start":
		ft_start(lst, sock, "")
	elif data == "stop":
		ft_stop(lst, sock, "")
	else:
		print("nothing matched " + data)
