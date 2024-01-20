# Chatroom-Application
Chatroom application developed in two versions: one using TCP protocol and the other using UDP protocol.

# TCP protocol:
•	TCP: reliable, byte stream-oriented
•	server must have created socket (door) that welcomes client’s contact.
•	Creating TCP socket, specifying IP address, port number of server process.
•	Application viewpoint: TCP provides reliable, in-order byte-stream transfer (“pipe”) between client and server processes and UDP.

# UDP protocol: 
•	UDP: unreliable datagram 
•	sender explicitly attaches IP destination address and port # to each packet.
•	receiver extracts sender IP address and port# from received packet.
•	Application viewpoint: UDP provides unreliable transfer of groups of bytes (“datagrams”) between client and server processes


# Features:
•	Accept multiple client connections.
•	Allow clients to send messages to the server.
•	Broadcast messages from one client to all other connected clients.

# How to use:
1.	Run the server file first. Once sever is up and running, join via the clients with a username of your choosing in the arguments.
2.	For a client to exit the group chat, type “exit” into the chat.
3.	Server will automatedly close down once all clients have left the server.
