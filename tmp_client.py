import socket,sys

sock_addr = "./socket"
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('client connecting to {}'.format(sock_addr))

try :
    sock.connect(sock_addr)
except socket.error:
    print >>sys.stderr
    sys.exit(1)

try :
    #send message
    message = "Hello"
    print('from client sending...')
    sock.sendall(message)
    size_rcvd = 0
    size_expected = len(message)
    while size_rcvd < size_expected :
        data = sock.recv(16)
        size_rcvd += len(data)
        print("received:>>{}".format(data))
finally:
    sock.close()