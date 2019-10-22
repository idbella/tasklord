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

def read(sock):
    strdata = "";
    while not strdata.endswith("end\n"):
        data = sock.recv(1)
        strdata = strdata + str(data, "UTF-8");
    strdata = strdata[:-4];
    print(strdata, end='')

try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(socket_addr)
except socket.error:
    print("error connecting to socket:: {}".format(socket_addr), file=sys.stderr)
    sys.exit(1)

def start(action):
    sock.sendall(action)
    read(sock)

def status(action):
    sock.sendall(action)
    read(sock)


def restart(action):
    sock.sendall(action)
    read(sock)

def stop(action):
    sock.sendall(action)
    read(sock)

def reload(action):
    sock.sendall(action)
    read(sock)

def exit(action):
    #close connection and exit
    print("exit")
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
    if action[0] != "exit" and action[0] != "status" and len(action) < 2:
        print("Missing arguments") #print help
        continue
    if builtins.get(action[0]):
        builtins[action[0]](pickle.dumps(action, pickle.HIGHEST_PROTOCOL))
        continue
    print("No such command: {}".format(action), file=sys.stderr)
