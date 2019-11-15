# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    listener.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 19:16:04 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/15 16:18:26 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pickle
from daemon import builtins
import logger

def listen(sock):
	while True :
		try:
			data = sock.recv(2048)
		except:
			logger.log("enabel to receive data from socket\n")
			sock.close()
			break
		if data:
			array = pickle.loads(data)
			br = builtins.ft_builtin(array, sock)
			sock.sendall(bytes("end\n", 'UTF-8'));
			if br:
				break
		else:
			break
