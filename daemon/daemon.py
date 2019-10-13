# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    daemon.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sid-bell <sid-bell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/12 18:21:28 by sid-bell          #+#    #+#              #
#    Updated: 2019/10/13 16:18:58 by sid-bell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys

def ft_daemon():
    pid = os.fork()

    if pid == 0:
        os.setsid()
        sys.stdout.close
        sys.stdin.close
        sys.stderr.close
    else:
        print("pid = " + str(pid), file=sys.stderr)
        exit(0)
