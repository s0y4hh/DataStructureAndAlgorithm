# creat a port scanner using socket module

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# define the port to connect
port = 9999

# connect to the server on local computer
s.connect((host, port))

# receive no more than 1024 bytes

msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))
