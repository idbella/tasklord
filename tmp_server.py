import socket,os,sys

# def init_server():
# check if socket already exists.
sock_addr = "./socket"
try :
    os.unlink(sock_addr)
except OSError:
    if os.path.exists(sock_addr):
        raise
#create socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print("starting on {}".format(sock_addr))
sock.bind(sock_addr)
sock.listen(1)
while True :
    print("waiting for a connection")
    connection, client_addr = sock.accept()
    try :
        while True :
            data = connection.recv(16)
            print("received {}".format(data))
            if data:
                print("sending it back...")
                connection.sendall(data)
            else:
                print("not receiving anything from {}".format(client_addr))
                break
    finally:
        connection.close()
# init_server()