# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    handler.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:17:37 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/12 21:13:39 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal, os, sys

def handler(sig, fr):
    pid, status = os.waitpid(-1, os.WNOHANG)
    print("proccess " + str(pid) + " exited with " + str(status))

def ft_handle_sigchild():
    signal.signal(signal.SIGCHLD, handler)
