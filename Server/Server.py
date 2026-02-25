import socket
import os
HOST = '127.0.0.1'
PORT = 4000

#FILE_NAME = "test.txt"
MAX_MESSAGE_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Server started")
conn, addr = s.accept()
print("Client connected:", addr)


path = input("Enter file path: ")
filename = os.path.basename(path)
name, ext = os.path.splitext(filename)

conn.send((name+ "\n").encode())
conn.send((ext+ "\n").encode())

f = open(path, "rb")
while True:
    data = f.read(MAX_MESSAGE_SIZE)
    if not data:
        break
    conn.send(data)

f.close()
conn.close()
s.close()

print("File sent")