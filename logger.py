# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/21 19:33:55 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/22 23:49:34 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os
from datetime import datetime

def log(data):
    now = datetime.now()
    data = now.strftime("%d/%m/%Y %H:%M:%S") + " : " + data
    os.write(3, bytes(data, 'UTF-8'))

def init_logger():
    fd = os.open("log", os.O_WRONLY|os.O_APPEND|os.O_CREAT)
    os.dup2(fd, 3)