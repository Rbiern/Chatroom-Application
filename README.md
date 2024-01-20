# Chatroom-Application
Chatroom application developed in two versions: one using TCP protocol and the other using UDP protocol.

# TCP protocol:
•	TCP: reliable, byte stream-oriented <br />
•	server must have created socket (door) that welcomes client’s contact. <br />
•	Creating TCP socket, specifying IP address, port number of server process. <br />
•	Application viewpoint: <br />
      TCP provides reliable, in-order byte-stream transfer (“pipe”) between client and server processes and UDP. <br />

# UDP protocol: 
•	UDP: unreliable datagram <br />
•	sender explicitly attaches IP destination address and port # to each packet. <br />
•	receiver extracts sender IP address and port# from received packet. <br />
•	Application viewpoint: <br />
    UDP provides unreliable transfer of groups of bytes (“datagrams”) between client and server processes. <br />


# Features:
•	Accept multiple client connections. <br />
•	Allow clients to send messages to the server. <br />
•	Broadcast messages from one client to all other connected clients. <br />

# How to use:
1.	Run the server file first. Once sever is up and running, join via the clients with a username of your choosing in the arguments.
2.	For a client to exit the group chat, type “exit” into the chat.
3.	Server will automatedly close down once all clients have left the server.
![Capture](https://github.com/Rbiern/Chatroom-Application/assets/156489385/187200ef-f89c-40d9-9a4c-a80c75841ee5)
