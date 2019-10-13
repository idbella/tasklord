#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    controller.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yoyassin <yoyassin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 10:15:23 by yoyassin          #+#    #+#              #
#    Updated: 2019/10/13 10:15:23 by yoyassin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, sys, readline, os, loader, re, pickle

#initializing connection
socket_addr = loader.loadjson()['socket']

try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(socket_addr)
except socket.error:
    print("error connecting to socket:: {}".format(socket_addr), file=sys.stderr)
    sys.exit(1)

def start(action):
    sock.sendall(action)

def status(action):
    sock.sendall(action)

def restart(action):
    sock.sendall(action)

def stop(action):
    sock.sendall(action)

def reload(action):
    sock.sendall(action)

def exit(action):
    #close connection and exit
    sock.close()
    sys.exit(0)

builtins = {'start': start,
            'status': status,
            'restart': restart,
            'stop': stop,
            'reload': reload,
            'exit': exit}

#controller loop

def validate_line(line):
    actions = line.split()
    patt = re.compile('^[a-zA-Z0-9]+$')
    for action in actions:
        if bool(re.match(patt, action)) :
            continue 
        else :
            return None
    return actions

while True:
    line = input('Taskmasterctl $> ').strip()
    if not line:
        continue
    action = list(validate_line(line))
    if not action:
        print("Invalid syntax.")
        continue
    if builtins.get(action[0]):
        builtins[action[0]](pickle.dumps(action, pickle.HIGHEST_PROTOCOL))
        data = sock.recv(100)
        print(str(data, "UTF-8") + "$")
        continue
    print("No such command: {}".format(action), file=sys.stderr)
