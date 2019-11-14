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
import signal
from app import App

#initializing connection

def read(sock):
    strdata = "";
    while not strdata.endswith("end\n"):
        data = sock.recv(1)
        strdata = strdata + str(data, "UTF-8");
    strdata = strdata[:-4];
    print(strdata, end='')

def init_conn():
    status , json = loader.loadjson(True);
    socket_addr = json['socket']
    try:
        App.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        App.socket.connect(socket_addr)
    except socket.error:
        print("error connecting to socket:: {}".format(socket_addr), file=sys.stderr)
        sys.exit(1)

def start(action):
    App.socket.sendall(action)
    read(App.socket)

def status(action):
    App.socket.sendall(action)
    read(App.socket)

def restart(action):
    App.socket.sendall(action)
    read(App.socket)

def stop(action):
    App.socket.sendall(action)
    read(App.socket)

def reload(action):
    App.socket.sendall(action)
    read(App.socket)
    App.socket.close()
    init_conn()

def ft_exit(action):
    #close connection and exit
    print("exit")
    App.socket.close()
    sys.exit(0)

builtins = {'start': start,
            'status': status,
            'restart': restart,
            'stop': stop,
            'reload': reload,
            'exit': ft_exit}

#controller loop

def validate_line(line):
    actions = line.split()
    patt = re.compile('^[a-zA-Z0-9]+:?[a-zA-Z0-9]+$')
    for action in actions:
        if bool(re.match(patt, action)) :
            continue 
        else :
            return ""
    return actions

def sighandler(sig, frame):
    ft_exit(None)

signal.signal(signal.SIGINT, sighandler)
init_conn()

while True:
    line = input('Taskmasterctl $> ')
    if not line:
        continue
    line = line.strip()
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
