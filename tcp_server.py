import socket
import threading


def handleClients(clientSocket, clientUsername, address):
    while True:
        try:
            clientMsg = clientSocket.recv(1024).decode()
            if clientMsg == "disconnect":
                clients.remove(clientSocket)
                clientSocket.close()
                print(f"User {clientUsername} left from address:{address}")
                if not clients:
                    server_socket.close()
                break
            else:
                print(f"Message received from {address}: {clientMsg}")
                for client in clients:
                    client.send(clientMsg.encode())
        except:
            clients.remove(clientSocket)
            clientSocket.close()
            break


def serverRuntime(serverSocket, serverPort):
    print("CHATROOM")
    print(f"I am ready to receive connections on port {serverPort}")

    while True:
        try:
            clientSocket, address = serverSocket.accept()
            clients.append(clientSocket)

            clientUsername = clientSocket.recv(1024).decode()
            print(f"User {clientUsername} joined from address:{address}")

            clientConnection = threading.Thread(target=handleClients, args=(clientSocket, clientUsername, address))
            clientConnection.start()

        except:
            print("interrupt received: shutting down\nserver shut down")
            break


if __name__ == "__main__":
    run = True
    server_port = 9301
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a TCP socket.
    server_socket.bind(('127.0.0.1', server_port))
    server_socket.listen(5)

    clients = []
    serverRuntime(server_socket, server_port)