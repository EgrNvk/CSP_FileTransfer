import socket

HOST = '127.0.0.1'
PORT = 4000

#FILE_NAME = "received.txt"
MAX_MESSAGE_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to server")
name = b""
while True:
    b = s.recv(1)
    if b == b"\n":
        break
    name += b
name = name.decode()

ext = b""
while True:
    b = s.recv(1)
    if b == b"\n":
        break
    ext += b
ext = ext.decode()

filename = name + ext

f = open(filename, "wb")

while True:
    data = s.recv(MAX_MESSAGE_SIZE)
    if not data:
        break
    f.write(data)

f.close()
s.close()

print("File received")