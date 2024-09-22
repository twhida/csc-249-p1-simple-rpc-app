#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#function for understanding the order from input
def understand(client_order):
    order = client_order.split(",")
    order_type = order[0].strip()

    if order_type == "scoop":
        flavor = order[1].strip()
        if len(order) > 1:
            syrup = order[2].strip()
            if syrup == "no_syrup":
                return f"Here is your {flavor} {order_type}!"
            if syrup == "chocolate_syrup":
                return f"Here is your {flavor} {order_type} with chocolate syrup!"
            if syrup == "cherry_syrup":
                return f"Here is your {flavor} {order_type} with cherry syrup!"
        else:
            return "Here is your scoop of mystery flavor... Please try ordering again!"
    elif order_type == "milkshake":
        flavor = order[1].strip()
        if len(order) > 1:
            syrup = order[2].strip()
            if syrup == "no_syrup":
                return f"Here is your {flavor} {order_type}!"
            if syrup == "chocolate_syrup":
                return f"Here is your {flavor} {order_type} with chocolate syrup!"
            if syrup == "cherry_syrup":
                return f"Here is your {flavor} {order_type} with cherry syrup!"
        else:
            return "Here is your milkshake with mystery flavor... Please try ordering again!"
    elif order_type == "chipwich":
        flavor = order[1].strip()
        if len(order) > 1:
            syrup = order[2].strip()
            if syrup == "no_syrup":
                return f"Here is your {flavor} {order_type}!"
            if syrup == "chocolate_syrup":
                return f"Here is your {flavor} {order_type} with chocolate syrup!"
            if syrup == "cherry_syrup":
                return f"Here is your {flavor} {order_type} with cherry syrup!"
        else:
            return "Here is your chipwich with mystery flavor... Please try ordering again!"
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
            #this should be the decoded order
            client_order = data.decode('utf-8')
            print(f"Received client order: '{client_order}' Current bytes: [{len(data)} bytes]\n")

            #here it should also give back the decoded order
            order_fulfillment = understand(client_order)
            print(f"Saying'{order_fulfillment}' to the to customer!\n")
            conn.sendall(order_fulfillment.encode('utf-8'))

print("Really Pretty Cool ice cream has been served, order complete! Closing shop...\n")
