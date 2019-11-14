# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/21 15:11:40 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/14 15:30:17 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class App:
	address = None
	socket = 0
	lst = None
	started_at = 0
	pid = 0
	status = "STOPPED"
	state = 1
	original_name = None
	name = None
	cmd = None
	argv = None
	numprocs = 1
	umask = 644
	workingdir = "/tmp"
	autostart = False
	autorestart = "unexpected"
	exitcodes = [0]
	startretries = 1
	starttime = 0
	stopsignal = 15
	stoptime = 10
	stdout = None
	stderr = None
	env = []
	RUNNING = 0
	STOPED = 1
	FAILED = 2
	DONE = 3
	failtimes = 0

def ft_send(msg, sock):
	msgutf8 = bytes(msg, 'UTF-8')
	sock.sendall(msgutf8)
