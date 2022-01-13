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

                            if branch[1] == "shift":
                                branch[1] = Key.shift

                            elif branch[1] == "alt":
                                branch[1] = Key.alt

                            elif branch[1] == "cmd":
                                branch[1] = Key.cmd
                            
                            elif branch[1] == "ctrl":
                                branch[1] = Key.ctrl

                            elif branch[1] == "tab":
                                branch[1] = Key.tab

                            elif branch[1] == "esc":
                                branch[1] = Key.esc

                            elif branch[1] == "enter":
                                branch[1] = Key.enter

                            elif branch[1] == "backspace":
                                branch[1] = Key.backspace

                            elif branch[1] == "del":
                                branch[1] = Key.delete

                            elif branch[1] == "up":
                                branch[1] = Key.up
                            
                            elif branch[1] == "down":
                                branch[1] = Key.down

                            elif branch[1] == "left":
                                branch[1] = Key.left

                            elif branch[1] == "right":
                                branch[1] = Key.right

                            elif branch[1] == "f1":
                                branch[1] = Key.f1

                            elif branch[1] == "f2":
                                branch[1] = Key.f2

                            elif branch[1] == "f3":
                                branch[1] = Key.f3

                            elif branch[1] == "f4":
                                branch[1] = Key.f4

                            elif branch[1] == "f5":
                                branch[1] = Key.f5

                            elif branch[1] == "f6":
                                branch[1] = Key.f6

                            elif branch[1] == "f7":
                                branch[1] = Key.f7

                            elif branch[1] == "f8":
                                branch[1] = Key.f8

                            elif branch[1] == "f9":
                                branch[1] = Key.f9

                            elif branch[1] == "f10":
                                branch[1] = Key.f10

                            elif branch[1] == "f11":
                                branch[1] = Key.f11

                            elif branch[1] == "f12":
                                branch[1] = Key.f12

                            else:
                                data_branches.remove(branch)

                            convert(branch)

