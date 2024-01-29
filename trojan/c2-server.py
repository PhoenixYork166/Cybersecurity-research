##!/usr/bin/python3
import socket
import base64
import random
from string import ascii_lowercase

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
# Listen on localhost port 1337
s.bind(("127.0.0.1", port))

# Queue up to 5 requests
s.listen(5)

print(f"Listening on {port}")

while True:
    # Establish a connection
    clientsocket, client_ip = s.accept()
    print("[+] Received a connection from -> {}".format(client_ip))
    
    # Get the encoded data
    # 4096 bytes
    encoded_data = clientsocket.recv(4096)
    clientsocket.close()
    
    # Open a file with a random and insert the decoded data into it
    random_fd = open("".join(random.choices(ascii_lowercase, k = 10)), "w")
    # Base64 decode => write to file in UTF-8
    random_fd.write(base64.b64decode(encoded_data).decode("UTF-8"))
    random_fd.close()

