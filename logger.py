# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/21 19:33:55 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/21 20:22:05 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os

def log(data):
    os.write(3, bytes(data, 'UTF-8'))

def init_logger():
    fd = os.open("log", os.O_WRONLY|os.O_APPEND|os.O_CREAT)
    os.dup2(fd, 3)