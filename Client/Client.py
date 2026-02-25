import socket

HOST = '127.0.0.1'
PORT = 4000

FILE_NAME = "received.txt"
MAX_MESSAGE_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to server")

f = open(FILE_NAME, "wb")

while True:
    data = s.recv(MAX_MESSAGE_SIZE)
    if not data:
        break
    f.write(data)

f.close()
s.close()

print("File received")