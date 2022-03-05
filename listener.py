import socket
import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

def convert(branch):

    sep = "__"
    
    if branch[0].upper() == "PRESS":
        keyboard.press(branch[1])

    if branch[0].upper() == "RELEASE":
        keyboard.release(branch[1])

    if branch[0].upper() == "TYPE":
        if sep in branch[1]:
            branch[1] = branch[1].replace(sep, " ")
        for char in branch[1]:
            keyboard.press(char)
            keyboard.release(char)

    if branch[0].upper() == "SLEEP":
        sleep(int(branch[1]))

def get_key(key):

    switcher = {
        "shift": Key.shift,
        "alt": Key.alt,
        "cmd": Key.cmd,
        "ctrl": Key.ctrl,
        "tab": Key.tab,
        "esc": Key.esc,
        "enter": Key.enter,
        "backspace": Key.backspace,
        "delete": Key.delete,
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right,
        "f1": Key.f1,
        "f2": Key.f2,
        "f3": Key.f3,
        "f4": Key.f4,
        "f5": Key.f5,
        "f6": Key.f6,
        "f7": Key.f7,
        "f8": Key.f8,
        "f9": Key.f9,
        "f10": Key.f10,
        "f11": Key.f11,
        "f12": Key.f12
    }

    return switcher.get(key, None)

ip = "0.0.0.0"
port = 1234
s = socket.socket()
s.bind((ip, port))
while True:
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")
        while True:
            data = conn.recv(1024 * 14)
            data = data.decode("utf8")

            if data.upper() == "CLOSE;":
                conn.close()
                print (f"{addr} disconnected.")
                break
            
            else:
                data = data.split(";")
                data_branches = []

                for part in data:
                    new_branch = part.split()
                    data_branches.append(new_branch)

                data_branches.pop()

                for branch in data_branches:

                    if len(branch) > 2 or len(branch) < 2:
                        data_branches.remove(branch)

                    else:

                        if len(branch[1]) > 1 or len(branch[1]) < 1:

                            key = get_key(branch[1])

                            if key != None:
                                branch[1] = key

                            else:
                                data_branches.remove(branch)

                            convert(branch)

