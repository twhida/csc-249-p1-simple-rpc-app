#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

#introduction, connection confirmation
print("Welcome to Tomoko's Really Pretty Cool (RPC) Ice Cream Stand!\n")
print("Customer identified! - Connecting you to server", HOST, "and port...", PORT)

#initalizing arguments/parameters for operations
#these arguments will be updated with user input
order_type = ""
size = ""
flavor = ""
syrup = ""
milk = ""
cookie = ""

#order type is updated first, and handles misspelling or empty inputs
while order_type not in ["scoop", "milkshake", "chipwich"]:
    order_type = input("Would you like a scoop, milkshake, or chipwich?\n")   
    if order_type not in ["scoop", "milkshake", "chipwich"]:
        print("I didn't quite catch that! Please choose either scoop, milkshake, or chipwich: ")

    #arguments for scoop order type are updated and include size, flavor, and choice of syrup
    #error handling implemented with if statements!
    if order_type == "scoop":
        while size not in ["small", "medium", "large"]:
            size = input("Specify the cup size: small, medium, large: \n")
            if size not in ["small", "medium", "large"]:
                print("I didn't quite catch that! Please choose either small, medium, or large: \n" )
        
        while flavor not in ["strawberry", "chocolate", "vanilla"]:
            flavor = input("Specify a flavor: strawberry, chocolate, vanilla: \n")
            if flavor not in ["strawberry", "chocolate", "vanilla"]:
                print("I didn't quite catch that! Please choose either strawberry, chocolate, vanilla: \n")

        while syrup not in ["no syrup", "chocolate syrup", "cherry syrup"]:
            syrup = input("Choose a syrup: no syrup, chocolate syrup, or cherry syrup: \n")
            if syrup not in ["no syrup", "chocolate syrup", "cherry syrup"]:
                print("I didn't quite catch that! Please choose either no syrup, chocolate syrup, or cherry syrup: \n")

    #arguments for milkshake order type are updated and include flavor, milk type, and choice of syrup
    #error handling implemented with if statements!
    elif order_type == "milkshake":
        while flavor not in ["strawberry", "chocolate", "vanilla"]:
            flavor = input("Specify a flavor: strawberry, chocolate, vanilla: \n")
            if flavor not in ["strawberry", "chocolate", "vanilla"]:
                print("I didn't quite catch that! Please choose either strawberry, chocolate, vanilla: \n")
        
        while milk not in ["dairy milk", "oat milk", "almond milk", "soy milk"]:
            milk = input("Choose your milk or alternative: dairy milk, oat milk, almond milk, or soy milk: \n")
            if milk not in ["dairy milk", "oat milk", "almond milk", "soy milk"]:
                print("I didn't quite catch that! Please choose either dairy milk, oat milk, almond milk, or soy milk: \n")
        
        while syrup not in ["no syrup", "chocolate syrup", "cherry syrup"]:
            syrup = input("Choose a syrup: no syrup, chocolate syrup, or cherry syrup: \n")
            if syrup not in ["no syrup", "chocolate syrup", "cherry syrup"]:
                print("I didn't quite catch that! Please choose either no syrup, chocolate syrup, or cherry syrup: \n")

    #arguments for chipwich order type are updated and include flavor and choice of cookie
    #error handling implemented with if statements!
    elif order_type == "chipwich":
        while flavor not in ["strawberry", "chocolate", "vanilla"]:
            flavor = input("Specify a flavor: strawberry, chocolate, vanilla: \n")
            if flavor not in ["strawberry", "chocolate", "vanilla"]:
                print("I didn't quite catch that! Please choose either strawberry, chocolate, vanilla: \n")
        
        while cookie not in ["chocolate chip", "oatmeal raisin", "sugar cookie", "snickerdoodle"]:
            cookie = input("Choose the cookies for your ice cream sandwich: chocolate chip, oatmeal raisin, sugar cookie, or snickerdoodle: \n")
            if cookie not in ["chocolate chip", "oatmeal raisin", "sugar", "snickerdoodle"]:
                print("I didn't quite catch that! Please choose either chocolate chip, oatmeal raisin, sugar cookie, or snickerdoodle: \n")

#MSG message created based on order type
if order_type == "scoop":
    MSG = f"{order_type},{size},{flavor},{syrup}"
elif order_type == "milkshake":
    MSG = f"{order_type},{flavor},{milk},{syrup}"
elif order_type == "chipwich":
    MSG = f"{order_type},{flavor},{cookie}"

#error handling for socket connection (used google to understand which exceptions to use)
#send order message MSG
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established! 'You ordered: {MSG}'")
        s.sendall(bytes(MSG, 'utf-8'))
        print("Ice cream order sent, thank you for your patience!\n")
        data = s.recv(1024)
except ConnectionRefusedError:
    print("It looks there's no one to take your order... See if the shop is actually open.")
    exit(1)
except Exception as e:
    print(f"Something is wrong with the shop's system... come back later and try ordering again! The sign on the door says: {e}")
    exit(1)

#message recieved from the server
#closing upon recieving the message from server
print(f"Order up! Your order is ready: '{data!r}' Current bytes: [{len(data)} bytes] Thank you for your visit!\n")
print("Your order was fulfilled. Time for a Lactaid?\n")
