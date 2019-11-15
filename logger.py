# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/21 19:33:55 by sid-bell          #+#    #+#              #
#    Updated: 2019/11/15 16:34:13 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os
from datetime import datetime
from app import App

def log(data):
    now = datetime.now()
    data = now.strftime("%d/%m/%Y %H:%M:%S") + " : " + data
    os.write(3, bytes(data, 'UTF-8'))

def init_logger():
    App.logfilefd = os.open("log", os.O_WRONLY | os.O_APPEND | os.O_CREAT)
