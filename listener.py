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
            data = conn.recv(1024)
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

                    if branch[1] == "shift":
                        branch[1] = Key.shift

                    if branch[1] == "alt":
                        branch[1] = Key.alt

                    if branch[1] == "cmd":
                        branch[1] = Key.cmd
                    
                    if branch[1] == "ctrl":
                        branch[1] = Key.ctrl

                    if branch[1] == "tab":
                        branch[1] = Key.tab

                    if branch[1] == "esc":
                        branch[1] = Key.esc

                    if branch[1] == "enter":
                        branch[1] = Key.enter

                    if branch[1] == "backspace":
                        branch[1] = Key.backspace

                    if branch[1] == "up":
                        branch[1] = Key.up
                    
                    if branch[1] == "down":
                        branch[1] = Key.down

                    if branch[1] == "left":
                        branch[1] = Key.left

                    if branch[1] == "right":
                        branch[1] = Key.right

                    if branch[1] == "f1":
                        branch[1] = Key.f1

                    if branch[1] == "f2":
                        branch[1] = Key.f2

                    if branch[1] == "f3":
                        branch[1] = Key.f3

                    if branch[1] == "f4":
                        branch[1] = Key.f4

                    if branch[1] == "f5":
                        branch[1] = Key.f5

                    if branch[1] == "f6":
                        branch[1] = Key.f6

                    if branch[1] == "f7":
                        branch[1] = Key.f7

                    if branch[1] == "f8":
                        branch[1] = Key.f8

                    if branch[1] == "f9":
                        branch[1] = Key.f9

                    if branch[1] == "f10":
                        branch[1] = Key.f10

                    if branch[1] == "f11":
                        branch[1] = Key.f11

                    if branch[1] == "f12":
                        branch[1] = Key.f12

                    convert(branch)

