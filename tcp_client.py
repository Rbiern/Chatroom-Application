import argparse
import socket
import sys
import threading


def getMsg():
    while True:
        try:
            serverMsg = client_socket.recv(1024).decode()
            if serverMsg == "close":
                client_socket.close()
                exit(1)
            else:
                sys.stdout.write('\r' + ' ' * (len(client_name + ': ')) + '\r')
                if client_name != serverMsg.split(':')[0]:
                    print(serverMsg)
                sys.stdout.write(client_name + ': ')
                sys.stdout.flush()
        except:
            print("socket of thread will terminate")
            break


def run(clientSocket, clientname):
    print(f"Client connected to server at {server_addr}:{server_port}")
    serverOutput = threading.Thread(target=getMsg)
    serverOutput.start()
    clientSocket.send(clientname.encode())

    try:
        sys.stdout.write(client_name + ': ')
        sys.stdout.flush()
        while True:
            msg = input()
            if msg == "exit":
                clientSocket.send("disconnect".encode())
                break
            else:
                msg = clientname + ": " + msg
                clientSocket.send(msg.encode())
    except:
        clientSocket.send("disconnect".encode())
        print('interrupt client: shutting down')

    clientSocket.close()
    print("Client Closing..........")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument('name')
    args = parser.parse_args()
    client_name = args.name
    server_addr = '127.0.0.1'
    server_port = 9301

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    client_socket.connect((server_addr, server_port))

    run(client_socket, client_name)