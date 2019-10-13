# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    init_socket.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:28:22 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/13 12:31:19 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket

def init_socket(file):
    try :
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    except :
        print("unable to creat socket")
        exit(1)
    try :
        sock.bind(file)
    except :
        print("unable to bind socket with " + file)
        exit(1)
    return sock
