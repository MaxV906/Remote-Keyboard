import socket

ip = "0.0.0.0"
port = 1234
s = socket.socket()
s.bind((ip, port))
s.listen()
conn, addr = s.accept()
print(f"Connected by: {addr}")
while True:
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)
