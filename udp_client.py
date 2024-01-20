import argparse
import socket
import sys
import threading
import random


def getMsg():
    while True:
        try:
            msg, addrPort = clientSocket.recvfrom(2048)
            sys.stdout.write('\r' + ' ' * (len(clientname + ': ')) + '\r')
            msg = msg.decode()
            if clientname != msg.split(':')[0]:
                print(msg)
            sys.stdout.write(clientname + ': ')
            sys.stdout.flush()
        except:
            print("socket of thread will terminate")
            break




def run(clientSocket, clientname, serverAddr, serverPort):
    print(f"Client connected to server at {serverAddr}:{serverPort}")
    clientSocket.bind(("", random.randint(1000, 6000)))

    serverData = threading.Thread(target=getMsg)
    serverData.start()

    clientSocket.sendto(clientname.encode(), (serverAddr, serverPort))

    while True:
        try:
            sys.stdout.write(clientname + ': ')
            sys.stdout.flush()

            text = input()
            if text == "exit":
                break

            clientSocket.sendto(text.encode(), (serverAddr, serverPort))

        except:
            print('interrupt client: shutting down')
            break
    clientSocket.sendto("exit".encode(), (serverAddr, serverPort))
    clientSocket.close()
    print("Client Closing..........")


if __name__ == "__main__":
    # Arguments: name address
    parser = argparse.ArgumentParser(description='argument parser')
    parser.add_argument('name')  # to use: python udp_client.py username
    args = parser.parse_args()
    clientname = args.name
    serverAddr = '127.0.0.1'
    serverPort = 9301
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    run(clientSocket, clientname, serverAddr, serverPort)  # Calling the function to start the client.