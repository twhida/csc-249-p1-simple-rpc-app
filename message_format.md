# Instructions

A document with a written description of your client-server message format (that is, a description of all implemented client and server messages, and how the various components of each message are represented). This document must also briefly summarize what your client-server application does, and provide examples of expected output for all implemented RPC operations. Your goal in writing this document should be to convey enough information in enough detail to allow a competent programmer without access to your source code to write either a new client that communicates properly with your server, or a new server that communicates properly with your client. 

This document should include at least five sections: Overview of Application, Client->Server Message Format, Server->Client Message Format, Example Output, Acknowledgments.

# Overview of Application 
In this project, my client-server application is represented as an ice cream shop, with the server as the shop, taking orders (messages), and the customer as the client, sending and receiving order receipts (messages) back. The forked source code defines the HOST IP address "127.0.0.1", the standard address used for loopback interfaces, and PORT number 65432.

## Server code
The server code imports the python socket library, and binds our socket to address family AF_INET (IPv4) and socket type SOCK_STREAM, which indicates that messages in the network will be transported using the TCP Protocol. Within this 'with' statement, the two-tuple socket binds to the indicated HOST and PORT as arguments, and is enters listening mode. Our s.accept() blocks execution until a connection is identified. And once a connection is identified, s.accept() returns a socket object for the connection and records the address of the client. This socket object communicates with the client. Within the server code, we enter another with statement, and once the connection socket object exists/is created, a message is printed to indicate that the client successfully connected with the server.

We now enter a while statement, and if there is data, we indicate that messages, given that there is data from a connection, can be up to 1024 bytes. IF there is no data, we break from the while statement. Proceeding with the case that there is data, we set the client's message to be the data, decoded using 'utf-8'. This is followed by a print message indicating the receival of data/message from the client, and an indication of the length of the data/message in bytes. Upon receiving the data, the server decodes the recieved message based on a function that turns the ice cream order (client's comma formatted data/messsage) into a sentence, and echoes the entire message back to the client before closing gracefully.

## Client code
The client code mirrors the server code, but sends MSG upon connecting to the server. A print statement indicating that the message was sent follows, and then the client waits to receive the echoed data from the server and captures it as ECHO_MSG. The ECHO_MSG that is received is the order formatted in sentence form as accomplished by the server code. This ECHO_MSG is printed upon receival, and the client closes gracefully at after printing.

# Client->Server Message Format
The client to server message format is supportedby while statements that prompt input from the terminal. All arguments, including the operation (order_type)indication are set to empty strings at the beginning of the program. As the order type as empty strings do not match the three possible order types "scoop", "milkshake", or "chipwich", the input is prompted. If the input by the user that overwrites the pre-set empty string does not match one of the three options again, a second message indicating that the input must be one of the three options is printed. This will happen for as long as the input does not match the order type options. 

If the order type matches "scoop", "milkshake", or "chipwich", the program enters if statements that run the same error-handling that the first order type input conducted. The messages requesting input for the scoop arguments will not proceed unless the input is matched with the options. The same is true for milkshake and chipwich order types. After these if and elif statements are complete, the message constant MSG is created based on the order type. If the order type was scoop, the recorded order type "scoop", size, flavor, and syrup are put together in a f-string using the arguments embedded in curly braces. For milkshake, the MSG is composed of order type "milkshake", flavor, milk type, and syrup, and for order type "chipwich", flavor and cookie follow. This MSG constant is sent to the server.

# Server-> Client Message Format
The server to client echo-back message format is structured in if statements according to order type. The order type is the string in the first index of the MSG array, and the subsequent arguments are in indeces with respect to the order type. If the order type is scoop, the subsequent indeces' strings are divided into arguments size, flavor, and syrup, and a string that incorporates these arguments into a cohesive sentence format is returned. The same process is true for order type milkshake and chipwich, but the arguments vary from the scoop arguments. If for any reason, the error handling in the client code was unsuccessful, there is an else return statement at the conclusion of the if statements that warns an unspecified order type.

# Example Output

## Ex 1: Milkshake
Indicated in the command_line_trace.txt file
Order example: milkshake, chocolate, almond milk, chocolate syrup

<echo-client.py terminal>
Order up! Your order is ready: 'b'Here is your chocolate milkshake with almond milk and chocolate syrup!'' Current bytes: [70 bytes] Thank you for your visit!

<echo-server.py terminal>
Saying 'Here is your chocolate milkshake with almond milk and chocolate syrup!' to the to customer!

<echo-client.py terminal>
Your order was fulfilled. Time for a Lactaid?

## Ex 2: Scoop
Order example: scoop, medium, strawberry, chocolate syrup

<echo-client.py terminal>
Order up! Your order is ready: 'b'Here is your medium strawberry scoop with chocolate syrup!'' Current bytes: [58 bytes] Thank you for your visit!

<echo-server.py terminal>
Saying 'Here is your medium strawberry scoop with chocolate syrup!' to the to customer!

<echo-client.py terminal>
Your order was fulfilled. Time for a Lactaid?

## Ex 3: Chipwich
Order example: scoop, medium, strawberry, chocolate syrup

<echo-client.py terminal>
OOrder up! Your order is ready: 'b'Here is your strawberry chipwich with sugar cookies!'' Current bytes: [59 bytes] Thank you for your visit!

<echo-server.py terminal>
Saying 'Here is your strawberry chipwich with sugar cookies!' to the to customer!

<echo-client.py terminal>
Your order was fulfilled. Time for a Lactaid?

# Acknowledgements
Socket Programming in Python (Guide): https://realpython.com/python-sockets/#background