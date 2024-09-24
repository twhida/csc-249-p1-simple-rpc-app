A document with a written description of your client-server message format (that is, a description of all implemented client and server messages, and how the various components of each message are represented). This document must also briefly summarize what your client-server application does, and provide examples of expected output for all implemented RPC operations. Your goal in writing this document should be to convey enough information in enough detail to allow a competent programmer without access to your source code to write either a new client that communicates properly with your server, or a new server that communicates properly with your client. 

This document should include at least five sections: Overview of Application, Client->Server Message Format, Server->Client Message Format, Example Output, Acknowledgments.

# Overview of Application 
In this project, my client-server application is represented as an ice cream shop, with the server as the shop, taking orders (messages), and the customer as the client, sending and receiving order receipts (messages) back. The forked source code defines the HOST IP address "127.0.0.1", the standard address used for loopback interfaces, and PORT number 65432.

The server code imports the python socket library, and binds our socket to address family AF_INET (IPv4) and socket type SOCK_STREAM, which indicates that messages in the network will be transported using the TCP Protocol. Within this 'with' statement, the two-tuple socket binds to the indicated HOST and PORT as arguments, and is enters listening mode. Our s.accept() blocks execution until a connection is identified. And once a connection is identified, s.accept() returns a socket object for the connection and records the address of the client. This socket object communicates with the client. Once the connection socket object is created, a message is printed to indicate that the client successfully connected with the server.

# Client->Server Message Format


# Server-> Client Message Format


# Example Output


# Acknowledgements
Socket Programming in Python (Guide): https://realpython.com/python-sockets/#background