import socket
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()

ip = "0.0.0.0"
port = 1234
s = socket.socket()
s.bind((ip, port))
s.listen()
conn, addr = s.accept()
with conn:
    print(f"Connected by: {addr}")
    while True:
        data = conn.recv(1024)
        data = data.decode("utf8")
        print(data)

        for char in data:
            keyboard.press(char)
            keyboard.release(char)
