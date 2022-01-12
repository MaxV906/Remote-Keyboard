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
            key_combination = input("\nChoose keys:\n1)Enter\n2)Backspace\n3)alt+f4\n4)ctrl+shift+esc\n5)alt+tab\n6)cmd\n7)tab\n8)up arrow\n9)down arrow\n10)left arrow\n11) right arrow\nYour answer: ")
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
