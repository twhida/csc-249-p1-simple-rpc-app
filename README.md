# CSC 249 – Programming Assignment 1 – Simple RPC Client-Server App

## Your First Network Application

Building distributed network applications in Python is fun!

For your first experience building a simple network application in Python, you will start with Python code taken from an online tutorial: Socket Programming in Python (Guide) by Nathan Jennings, available online at https://realpython.com/python-sockets/. 

The Jennings tutorial opens with the design and implementation of an “Echo Client and Server.” In this simple application, the server is launched first on the local machine and makes calls to the Python sockets library to wait for a new connection. In a separate process on the same machine, the client establishes a network connection to the server and sends a single text message, “Hello, world” (you knew that was coming, right?) The server receives this message and sends it right back (“echoes”) to the client. The server exits after echoing the message, and the client exits after receiving the echo message. You are strongly encouraged to study the code, try running it, and make sure you understand how it works. I’ve placed the code in this Git repo [https://github.com/bcheikes/csc249-p1-simple-rpc-app], which you are welcome to clone.

The echo application makes for a fine capability demonstration but isn’t very interesting. For this exercise, I want you to build something more interesting so you can get some practical experience with encoding, transmitting, receiving, decoding, and processing more complex messages.

What you will do is extend the echo-server into a “remote procedure call” (RPC) server. Conceptually, a RPC server accepts incoming network requests to perform some kind of computation, typically expressed as a “requested operation” along with one or more arguments. For example, a “basic math” RPC server could process one of four requested operations: add, subtract, multiply, or divide. Such a server might accept two integer arguments and reply to the client with a message containing the result of adding, subtracting, multiplying or dividing the arguments.

The main challenges for you in this exercise will be:
* Coming up with a creative set of requested operations that your RPC server will process.
* Designing a method for encoding client requests and arguments into a Python bytes object for transmission.
* Designing a method for decoding client requests on the server, processing them, and returning a response.

Like the echo application, your server should terminate after successfully processing a client message, and your client should terminate after successfully receiving a response to its request.

## Design requirements

Your server must be able to process two different requested operations. This means that an indication of the requested operation needs to be passed from client to server.

* Each requested operation must take at least two arguments. This means that you need to encode each argument in the request message, with an indication of where one argument “ends” and the next one “begins”.
* Your client must obtain the desired operation and its arguments either from keyboard input or from the command line.
* The client and the server applications must generate time-stamped output that documents when connections are made, when messages and sent and received, and what was sent and what was received.
* Source code of your client and server must be well documented. Comments should be sufficient to allow a third party to understand your code, run it, and confirm that it works.

## Deliverables

Your work on this project must be submitted for grading by **Wednesday Sep 27th at 11:56PM**. Extensions may be obtained by following the late submission policy [https://docs.google.com/document/d/1Fx0iviSFzelwKQWx-QmeSulg4MwX9xXS].

All work must be submitted in Gradescope.

You must submit these work products:

1. Source code for your client and server. Ideally, this will be a link to your public Git code repo.
2. A document with a written description of your client-server message format (that is, a description of all implemented client and server messages, and how the various components of each message are represented). This document must also briefly summarize what your client-server application does, and provide examples of expected output for all implemented RPC operations.
3. A command-line trace showing the client and server in operation. 

## Teamwork Policy

**For this project, all work must be performed individually – no team submissions will be allowed**. You are free to collaborate and exchange ideas, but each student must submit their own original work.

## Getting Help

There is plenty of self-help material out there to help you understand socket programming in Python. 

* Socket Programming in Python (Guide) by Nathan Jennings [https://realpython.com/python-sockets/]
* Python sockets library documentation [https://docs.python.org/3/library/socket.html]
* LinkedIn Learning (Smith College offers free access) – search “python sockets”
* Python sockets tutorials on YouTube [for example, try https://www.youtube.com/watch?v=3QiPPX-KeSc]. There are many!
* Slack messages in the #questions channel. Students are encouraged to help each other out – this is part of what “participation and engagement” means in the overall course grading rubric.
* Instructor and TA office hours!

## Grading Rubric

Your work on this project will be graded on a five-point scale. Fractional points may be awarded.

_0 pts:_ No deliverables were received by the due date or requested extension date.

_1 pt:_ Incomplete deliverables were received by the due date or extension date.

_2 pts:_ Required deliverables were received but are deficient in various ways (e.g., incomplete documentation, code doesn’t run)

_3 pts:_ Complete and adequate deliverables. Code runs but is deficient in various ways.

_4 pts:_ Code runs and does most but not all of what is required.

_5 pts:_ Nailed it. Complete deliverables, code runs and does what is required.


