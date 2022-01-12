import socket

s = socket.socket()
port = 1234

def main():
    while True:
        option = input("Choose a method:\n1)Send string\n2)Send keys\nYour answer: ")
        if option == "1":
            string = input("\nString you want to send: ")
            s.send(string.encode("utf8"))
        else:
            key_combination = input("\nChoose keys:\n1)alt+f4\n2)ctrl+shift+esc\n3)alt+tab\n4)cmd\n5)tab\n6)up arrow\n7)down arrow\n8)left arrow\n9) right arrow\nYour answer: ")
            string = "key-combination: " + str(int(key_combination) - 1)
            s.send(string.encode("utf8"))

while True:

    ip = input("Listener's ip: ")

    try:
        s.connect((ip, port))
        break

    except:
        print("Failed to connect.")

main()
