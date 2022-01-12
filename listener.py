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

        if data.startswith("key-combination:"):

            if "0" in data:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

            if "1" in data:
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)

            if "2" in data:
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)

            if "3" in data:
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)

            if "4" in data:
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

            if "5" in data:
                keyboard.press(Key.up)
                keyboard.release(Key.up)

            if "6" in data:
                keyboard.press(Key.down)
                keyboard.release(Key.down)

            if "7" in data:
                keyboard.press(Key.left)
                keyboard.release(Key.left)

            if "8" in data:
                keyboard.press(Key.right)
                keyboard.release(Key.right)

            if "9" in data:
                with keyboard.pressed(Key.alt):
                    keyboard.press(Key.f4)
                    keyboard.release(Key.f4)

            if "10" in data:
                with keyboard.pressed(Key.ctrl):
                    with keyboard.pressed(Key.shift):
                        keyboard.press(Key.esc)
                        keyboard.release(Key.esc)

            if "11" in data:
                with keyboard.pressed(Key.alt):
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)

            if "12" in data:
                with keyboard.pressed(Key.cmd):
                    keyboard.press("r")
                    keyboard.release("r")

        else:
            for part in data:
                for char in part:
                    keyboard.press(char)
                    keyboard.release(char)

