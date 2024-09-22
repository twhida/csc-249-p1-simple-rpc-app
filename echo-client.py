#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

print("Welcome to Tomoko's Really Pretty Cool (RPC) Ice Cream Stand!\n")


order_type = ""
size = ""
flavor = ""
syrup = ""
milk = ""
cookie = ""



while order_type not in ["scoop", "milkshake", "chipwich"]:
    order_type = input("Would you like your ice cream as a scoop, milkshake, or chipwich?\n")

while size not in ["small", "medium", "large"]:
    
if order_type == "scoop":
    size = input("Specify the cup size: small, medium, large")
    while size == "small" or size == "medium" or size == "large":
        flavor = input("Specify a flavor: strawberry, chocolate, vanilla")
    print("Scoop size was not recorded, please try again.")
    size = input("Please specify a size: small, medium, or large:\n")
        
    
MSG = f"{order_type},{size},{flavor}"

print("Customer identified! - Connecting you to server", HOST, "and port...", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established! 'You ordered: {MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("Ice cream order sent, thank you for your patience!\n")
    data = s.recv(1024)

print(f"Order up! Your order is ready: '{data!r}' Current bytes: [{len(data)} bytes] Thank you for your visit!\n")
print("Your order was fulfilled. Time for a Lactaid?\n")
