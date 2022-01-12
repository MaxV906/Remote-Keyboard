import socket

s = socket.socket()
port = 1234

def main():
    while True:
        command = input("Command: ")

        s.send(command.encode("utf8"))

        if command.upper() == "EXIT;":
            break

while True:

    ip = input("Listener's ip: ")

    try:
        s.connect((ip, port))
        break

    except:
        print("Failed to connect.")

main()
