import socket

s = socket.socket()
port = 1234

def main():
    while True:
        string = input("String you want to send: ")
        s.send(string.encode("utf8"))

while True:

    ip = input("Listener's ip: ")

    try:
        s.connect((ip, port))
        break

    except:
        print("Failed to connect.")

main()
