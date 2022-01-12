import socket

s = socket.socket()
port = 1234

def main():
    while True:
        option = input("\nChoose an option:\n\n1)Send a command\n2)Send a script\n0)Exit\nYour answer:")

        if option == "1":
            while  True:
                command = input("Command: ")

                if command.upper() == "BACK;":
                    break

                else:
                    s.send(command.encode("utf8"))
        
        if option == "2":
            script = input("Location to your script: ")

            try:
                f = open(script, "r")
                command = f.read()
                f.close()

                s.send(command.encode("utf8"))

            except:
                print("Failed to open the script.\n")

        if option == "0":
            s.send("CLOSE;".encode("utf8"))
            break

while True:

    ip = input("Listener's ip: ")

    try:
        s.connect((ip, port))
        break

    except:
        print("Failed to connect.")

main()
