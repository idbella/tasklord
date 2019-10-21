# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_builtins.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yoyassin <yoyassin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 19:23:05 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/13 21:07:55 by yoyassin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys
from daemon import runner

def ft_send(msg, sock):
	msgutf8 = bytes(msg, 'UTF-8')
	sock.sendall(msgutf8)

def ft_status(lst, sock, args):
	if 'all' in args :
		for app in lst:
			ft_send("{} {} {} {}".format(app.name, app.pid, app.status, app.started_at), sock)
	else :
		args = args[1:]
		for arg in args:
			print(">>>>>>arg<<<<<<{}".format(arg))
			try :
				app = lst[]
			ft_send("{} {} {} {}".format(app.name, app.pid, app.status, app.started_at), sock)

def ft_stop(lst, sock, args):
	for app in lst:
		ft_send("stopping " + app.name, sock)

def ft_start(lst, sock, args):
	for app in lst:
		runner.run(app, sock)

def ft_builtin(data, lst, sock):
	if data[0] == "status":
		ft_status(lst, sock, data)
		print('{}'.format(data))
	elif data[0] == "start":
		ft_start(lst, sock, "")
	elif data[0] == "stop":
		ft_stop(lst, sock, "")

def ft_startup(lst):
    for app in lst:
    	if app.autostart:
    		runner.run
