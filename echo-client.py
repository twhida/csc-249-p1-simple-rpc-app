#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
MSG = ("Welcome to Tomoko's Really Pretty Cool (RPC) Ice Cream Stand!\nFlavors: strawberry, chocolate, vanilla\nWe offer: scoop, milkshake, chipwich\nToppings: no_topping, whipped_cream, sprinkles\nPlease indicate your order by writing the flavor, ice cream type, and toppings (or lack thereof) in order.")

print("Customer identified! - Connecting you to server", HOST, "and port...", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established! sending your unique Really Pretty Cool order... '{MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("Ice cream order sent, thank you for your patience!")
    data = s.recv(1024)

print(f"Order up! Your order is ready: '{data!r}' You paid: [{len(data)} bytes] Thank you for your visit!")
print("Your oder was fulfilled. Time for a Lactaid?")
