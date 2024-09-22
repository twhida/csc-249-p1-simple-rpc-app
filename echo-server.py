#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#function for understanding the order from input
def understand(client_order):
    order = client_order.split(",")
    order_type = order[0].strip()

    if order_type == "scoop":
        if len(order) < 4:
            return "Your scoop order is missing your preferences! Please try again."
        size = order[1].strip()
        flavor = order[2].strip()
        syrup = order[3].strip()
        return f"Here is your {size} {flavor} {order_type} with {syrup}!"
        
    elif order_type == "milkshake":
        if len(order) < 4:
            return "Your milkshake order is missing your preferences! Please try again."
        flavor = order[1].strip()
        milk = order[2].strip()
        syrup = order[3].strip()
        return f"Here is your {flavor} {order_type} with {milk} and {syrup}!"

    elif order_type == "chipwich":
        if len(order) < 3:
            return "Your chipwich order is missing your preferences! Please try again."
        flavor = order[1].strip()
        cookie = order[2].strip()
        return f"Here is your {flavor} chipwich with {cookie} cookies!"
    
    else:
        return "You did not specify an order type! Please try ordering again."

print("Server starting - opening up shop at", HOST, "with our cool entryway door with model number", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Successfully opened shop: We are open to orders!\n")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            #receive order and decode
            client_order = data.decode('utf-8')
            print(f"Received client order: '{client_order}' Current bytes: [{len(data)} bytes]\n")

            #echo decoded order back to client
            order_fulfillment = understand(client_order)
            print(f"Saying '{order_fulfillment}' to the to customer!\n")
            conn.sendall(order_fulfillment.encode('utf-8'))

print("Really Pretty Cool ice cream has been served, order complete! Closing shop...\n")
