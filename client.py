import socket

s = socket.socket()
port = 1234

def main():
    while True:
        option = input("\nChoose a method:\n1)Send string\n2)Send keys\n0)Exit\nYour answer: ")
        if option == "0":
            break

        elif option == "1":
            string = input("\nString you want to send: ")
            s.send(string.encode("utf8"))

        elif option == "2":
            key_combination = input("\nChoose keys:\n1)Enter\n2)Backspace\n3)esc\n4)cmd\n5)tab\n6)up arrow\n7)down arrow\n8)left arrow\n9)right arrow\n10)alt+f4\n11)ctrl+shift+esc\n12)alt+tab\n13)cmd+r\nYour answer: ")
            string = "key-combination: " + str(int(key_combination) - 1)
            s.send(string.encode("utf8"))

        else:
            print("Please enter a valid option.")

while True:

    ip = input("Listener's ip: ")

    try:
        s.connect((ip, port))
        break

    except:
        print("Failed to connect.")

main()
