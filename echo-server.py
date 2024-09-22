#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("Server starting - opening up shop at ", HOST, "with our cool entryway door with model number ", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Successfully opened shop: We are open to orders!\n")
        while True:
            #data should be parsed/evaluated
            data = conn.recv(1024)
            if not data:
                break
            #this should be the decoded order
            print(f"Received client order: '{data!r}' Payment due: [{len(data)} bytes]\n")
            #here it should also give back the decoded order
            print(f"Serving '{data!r}' to the to customer!\n")
            conn.sendall(data)

print("Really Pretty Cool ice cream has been served, order complete! Closing shop...\n")
