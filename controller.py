#!/usr/bin/python
import socket, sys, readline, os
from loader import loadjson as ljson

#initializing connection
socket_addr = ljson()['socket']
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    sock.connect(socket_addr)
except socket.error:
    print("error connecting to socket:: {}".format(socket_addr), file=sys.stderr)
    sys.exit(1)

def start():
    msg = bytes("START", 'UTF-8')
    sock.sendall(msg)

def status():
    msg = bytes("STATUS", 'UTF-8')
    sock.sendall(msg)

def restart():
    msg = bytes("RESTART", 'UTF-8')
    sock.sendall(msg)

def stop():
    msg = bytes("STOP", 'UTF-8')
    sock.sendall(msg)

def reload():
    msg = bytes("RELOAD", 'UTF-8')
    sock.sendall(msg)

def exit():
    #close connection and exit
    sys.exit(0)

builtins = {'start': start,
            'status': status,
            'restart': restart,
            'stop': stop,
            'reload': reload,
            'exit': exit}

#controller loop

while True:
    action = input('Taskmasterctl $> ')
    if builtins.get(action):
        builtins[action]()
        continue
    print("No such command: {}".format(action), file=sys.stderr)
