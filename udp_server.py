import socket
import threading


def handleMsg(message, clientAddress):
    while True:
        if message == "exit":
            index = clients.index(clientAddress)
            user = userName[index]
            print(f"User {user} left from address:{clientAddress}")
            clients.remove(clientAddress)
            userName.remove(user)
            if not clients:
                serverSocket.close()
                print("interrupt received: shutting down\nserver shut down")
                break
            break
        else:
            print(f"Message received from {clientAddress}: {message}")
            index = clients.index(clientAddress)
            user = userName[index]
            for i in range(len(clients)):
                msg = user + ": " + message
                serverSocket.sendto(msg.encode(), clients[i])
        break


def run(serverSokect, serverPort):
    print("CHATROOM\n")
    serverSokect.bind(('127.0.0.1', serverPort))
    print(f"I am ready to receive connections on port {serverPort}")

    while True:
        try:
            message, clientAddress = serverSokect.recvfrom(2048)
            if clientAddress not in clients:
                clients.append(clientAddress)
                userName.append(message.decode())
                print(f"User {message.decode()} joined from address:{clientAddress}")
            else:
                clientThread = threading.Thread(target=handleMsg, args=(message.decode(), clientAddress))
                clientThread.start()
            if not clients:
                serverSokect.close()
                print("interrupt received: shutting down\nserver shut down")
                break
        except:
            serverSokect.close()
            print("interrupt received: shutting down\nserver shut down")
            break


if __name__ == "__main__":
    serverPort = 9301
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating a UDP socket.
    clients = []
    userName = []
    run(serverSocket, serverPort)

