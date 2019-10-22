# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    listener.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 19:16:04 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/21 14:43:59 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pickle
from daemon import builtins

def listen(sock, lst):
	while True :
		try:
			data = sock.recv(2048)
		except:
			sock.close()
			break
		if data:
			array = pickle.loads(data)
			builtins.ft_builtin(array, lst, sock)
			sock.sendall(bytes("end\n", 'UTF-8'));
		else:
			break
