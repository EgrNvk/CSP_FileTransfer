import socket

HOST = '127.0.0.1'
PORT = 4000

FILE_NAME = "test.txt"
MAX_MESSAGE_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Server started")
conn, addr = s.accept()
print("Client connected:", addr)

f = open(FILE_NAME, "rb")

while True:
    data = f.read(MAX_MESSAGE_SIZE)
    if not data:
        break
    conn.send(data)

f.close()
conn.close()
s.close()

print("File sent")