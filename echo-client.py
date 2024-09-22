#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

order_type = input("Would you like your ice cream as a scoop, milkshake, or chipwich?\n")
flavor = ("Specify a flavor: strawberry, chocolate, vanilla\n")
syrup = ("Would you like no_syrup, chocolate_syrup, or cherry_syrup?\n")

MSG = f"{order_type}:{flavor}:{syrup}"

print("Welcome to Tomoko's Really Pretty Cool (RPC) Ice Cream Stand!\n")
print("Customer identified! - Connecting you to server", HOST, "and port...", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established! '{MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("Ice cream order sent, thank you for your patience!\n")
    data = s.recv(1024)

print(f"Order up! Your order is ready: '{data!r}' You paid: [{len(data)} bytes] Thank you for your visit!\n")
print("Your order was fulfilled. Time for a Lactaid?\n")
