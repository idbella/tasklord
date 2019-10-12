# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    validate.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:28:28 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/12 18:28:43 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def validate(js) :
	try:
		lst = js['apps']
		for app in lst:
			name = app['name']
			cmd = app['cmd']
			if len(name) < 1:
				print("invalid name")
				exit(1)
			if len(cmd) < 2:
				print("invalid cmd path")
				exit(1)
			elif cmd[0] != '/':
				print("cmd path must be absolut")
				exit(1)
	except :
		print("error")
		exit(1)
