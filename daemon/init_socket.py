# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    init_socket.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:28:22 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/15 16:35:52 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, os
import logger

def init_socket(file):
	logger.log("initialize new socket\n") 
	if os.path.exists(file):
		os.unlink(file)
	try :
		sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	except :
		print("unable to create socket")
		exit(1)
	try :
		sock.bind(file)
	except :
		print("unable to bind socket with " + file)
		exit(1)
	return sock
